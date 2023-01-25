import numpy as np
import pandas as pd
import lifelines
from tqdm import tqdm


def calculate_logrank_test(
    tcga_datasets: list, return_value: str = "p-value"
) -> pd.DataFrame:

    results = []

    for tcga in tqdm(tcga_datasets):

        metadata = pd.read_csv(
            f"TCGA/TCGA-{tcga}-metadata.tsv", sep="\t", index_col=[0]
        )
        ssgsea = pd.read_csv(f"TCGA/TCGA-{tcga}-ssGSEA.tsv", sep="\t", index_col=[0])

        results += [
            calculate_logrank_for_one_dataset(metadata, ssgsea, tcga, return_value)
        ]

    return pd.concat(results, axis=1)


def calculate_logrank_for_one_dataset(
    metadata: pd.DataFrame,
    ssgsea: pd.DataFrame,
    tcga: str,
    return_value: str = "p-value",
) -> pd.Series:

    scores = {}

    for split_by in ssgsea.columns:

        up_ids = ssgsea[split_by] > np.median(ssgsea[split_by])
        up_score = metadata.loc[up_ids]
        down_score = metadata.loc[up_ids != True]

        logrank_test_score = lifelines.statistics.logrank_test(
            up_score["time"],
            down_score["time"],
            event_observed_A=up_score["event"],
            event_observed_B=down_score["event"],
        )

        if return_value == "p-value":
            scores[split_by] = logrank_test_score.p_value
        elif return_value == "test-statistic":
            scores[split_by] = logrank_test_score.test_statistic
        else:
            raise KeyError(
                "Invalid return_value: f{return_value}. Choose either p-value or test-statistic."
            )

    return pd.Series(scores, name=tcga)


if __name__ == "__main__":

    from parse_datasets import TCGA_DATASETS

    logrank_score = calculate_logrank_test(TCGA_DATASETS, return_value="p-value")

    logrank_score.reset_index().to_csv(
        f"TCGA/logrank-scores-p-value.tsv", sep="\t", index=False
    )

    logrank_score = calculate_logrank_test(TCGA_DATASETS, return_value="test-statistic")

    logrank_score.reset_index().to_csv(
        f"TCGA/logrank-scores-test-statistic.tsv", sep="\t", index=False
    )