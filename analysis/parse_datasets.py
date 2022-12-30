import os
import numpy as np
import pandas as pd
from tqdm import tqdm

TCGA_DATASETS = [
    "BLCA",
    "BRCA",
    "CESC",
    "COAD",
    "GBM",
    "HNSC",
    "KIRC",
    "KIRP",
    "LAML",
    "LGG",
    "LIHC",
    "LUAD",
    "LUSC",
    "OV",
    "PRAD",
    "READ",
    "SKCM",
    "STAD",
    "THCA",
    "UCEC",
]


def load_cancer_type():

    cancer = pd.read_csv(
        "raw-data/GSE62944_06_01_15_TCGA_24_CancerType_Samples.txt",
        sep="\t",
        header=None,
        index_col=[0],
    )
    cancer.index.name = "sample"
    cancer.columns = ["TCGA"]

    return cancer


def load_RNA_seq_expressions():
    return pd.read_csv(
        "raw-data/GSM1536837_06_01_15_TCGA_24.tumor_Rsubread_TPM.txt", sep="\t"
    )


def load_clinical_metadata():
    return pd.read_csv(
        "raw-data/GSE62944_06_01_15_TCGA_24_548_Clinical_Variables_9264_Samples.txt",
        sep="\t",
        index_col=[0],
    )


def parse_RNA_seq_data():

    cancer = load_cancer_type()
    expressions = load_RNA_seq_expressions()

    for tcga in tqdm(TCGA_DATASETS):

        if f"TCGA-{tcga}-expressions.tsv" in os.listdir("TCGA"):
            continue

        tcga_cols = cancer[cancer["TCGA"] == tcga].index.values
        drop_col = [
            expressions.columns[i]
            for i in range(1, len(expressions.columns))
            if expressions.columns[i] not in tcga_cols
        ]
        expressions.drop(drop_col, axis=1).to_csv(
            f"TCGA/TCGA-{tcga}-expressions.tsv", sep="\t", index=False
        )


def parse_metadata():

    cancer = load_cancer_type()
    clinical = load_clinical_metadata()

    survival_columns = [
        "death_days_to",
        "last_contact_days_to",
        "days_to_death",
        "days_to_last_followup",
        "vital_status",
    ]
    clinical.loc[survival_columns]

    clinical_surv = clinical.loc[survival_columns]

    def convert_to_int_array(x):
        y = []
        for i in x:
            try:
                int(i)
            except Exception:
                i = 0
            y += [int(i)]
        return y

    metadata = {}
    for patient in clinical.columns[2:]:
        temp = clinical_surv[patient]

        time_to_event = max(convert_to_int_array(temp.values[:-1]))
        event = int(temp.loc["vital_status"] == "Dead")

        metadata[patient] = [time_to_event, event]

    metadata = pd.DataFrame(metadata, index=["time", "event"]).T
    metadata.reset_index().to_csv("TCGA/metadata.tsv", sep="\t", index=False)

    for tcga in tqdm(TCGA_DATASETS):

        metadata.loc[cancer["TCGA"] == tcga].reset_index().to_csv(
            f"TCGA/TCGA-{tcga}-metadata.tsv", sep="\t", index=False
        )


if __name__ == "__main__":

    if "TCGA" not in os.listdir("./"):
        os.mkdir("TCGA")

    parse_metadata()

    parse_RNA_seq_data()