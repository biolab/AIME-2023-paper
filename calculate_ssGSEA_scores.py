import os
import json

import numpy as np
import pandas as pd
import scipy.stats as ss

from tqdm import tqdm


from single_sample_gsea import ss_gsea as ssGSEA
from parse_datasets import TCGA_DATASETS


def get_hallmark_genesets(expressed_genes, dir="."):

    with open(f"{dir}/data/h.all.v2022.1.Hs.json") as f:
        hallmark = json.load(f)

    return {
        name: set([g for g in hallmark[name]["geneSymbols"] if g in expressed_genes])
        for name in hallmark.keys()
    }


def calculate_ssGSEA(tcga: str):

    expressions = pd.read_csv(
        f"TCGA/TCGA-{tcga}-expressions.tsv", sep="\t", index_col=[0]
    ).T
    expressions = np.log(expressions + 1)
    expressions = (expressions - expressions.mean(axis=0)) / expressions.std(axis=0)
    expressions = expressions.dropna(axis=1)
    expressions = expressions.fillna(0)

    hallmark_genesets = get_hallmark_genesets(expressions.columns)

    expressions = expressions.T
    expressions.index.name = "gene"

    ssGSEA_scores = ssGSEA(expressions, hallmark_genesets)

    ssGSEA_scores.reset_index().to_csv(
        f"TCGA/TCGA-{tcga}-ssGSEA.tsv", sep="\t", index=False
    )


if __name__ == "__main__":

    for tcga in tqdm(TCGA_DATASETS):

        calculate_ssGSEA(tcga)
