import numpy as np
import pandas as pd
import lifelines
from tqdm import tqdm


def calculate_logrank_test(tcga_datasets) -> pd.DataFrame:

    results = []

    for tcga in tqdm(tcga_datasets):

        metadata = pd.read_csv(
            f"TCGA/TCGA-{tcga}-metadata.tsv", sep="\t", index_col=[0]
        )
        ssgsea = pd.read_csv(f"TCGA/TCGA-{tcga}-ssGSEA.tsv", sep="\t", index_col=[0])

        results += [calculate_logrank_for_one_dataset(metadata, ssgsea, tcga)]

    return pd.concat(results, axis=1)


def calculate_logrank_for_one_dataset(
    metadata: pd.DataFrame, ssgsea: pd.DataFrame, tcga: str
) -> pd.Series:

    scores = {}

    for split_by in ssgsea.columns:

        up_ids = ssgsea[split_by] > np.median(ssgsea[split_by])
        up_score = metadata.loc[up_ids]
        down_score = metadata.loc[up_ids != True]

        scores[split_by] = lifelines.statistics.logrank_test(
            up_score["time"],
            down_score["time"],
            event_observed_A=up_score["event"],
            event_observed_B=down_score["event"],
        ).p_value

    return pd.Series(scores, name=tcga)


if __name__ == "__main__":

    from parse_datasets import TCGA_DATASETS

    logrank_score = calculate_logrank_test(TCGA_DATASETS)

    logrank_score.reset_index().to_csv(
        f"TCGA/logrank-scores.tsv", sep="\t", index=False
    )
