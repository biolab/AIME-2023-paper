"""
Code author: Jaka Kokošar
"""
import numpy as np
import pandas as pd
import scipy.stats as ss
import numba as nb


def ssGSEA(df: pd.DataFrame, gene_sets: dict):
    """
    Parameters
    ----------
    df: pd.DataFrame
        Rows as genes, columns as samples
    gene_sets: dict
        Key as geneset name, value as genes in a geneset

    Return
    ------
    results: dict
        Key as geneset name, value as list of gene enrichment scores
    """

    alpha = 0.25

    @nb.njit(parallel=True)
    def _isin(a: np.ndarray, b: np.array):
        a_as1d = a.ravel()
        n = len(a_as1d)
        b = set(b)

        result = np.full(n, False)
        for i in nb.prange(n):
            result[i] = a_as1d[i] in b

        return result.reshape(a.shape)

    df_samples = df.loc[:, ~df.columns.isin(["gene"])]
    X = df_samples.values

    # rank normalize
    X = ss.rankdata(X, axis=0)

    # Get indexes of ranks in decreasing order
    ranks_decreasing_indexes = np.argsort(X, axis=0)[::-1]

    # z-transform
    X = (X - np.mean(X, axis=0)) / np.std(X, axis=0)
    X = np.abs(X)

    # rank weight
    X = X ** alpha

    # Sort ranks in decreasing order
    ranks_sorted_decreasing = np.take_along_axis(X, ranks_decreasing_indexes, axis=0)

    results = {}

    for gs_name, genes in gene_sets.items():
        # indexes of signature genes in the data
        gs_genes_index = np.where(df["gene"].isin(genes))[0]

        # Get positions of signatures genes in sorted ranks
        # gs_genes_to_rank_indexes = np.isin(ranks_decreasing_indexes, gs_genes_index, assume_unique=True)
        # gs_genes_to_rank_indexes = np.in1d(ranks_decreasing_indexes, gs_genes_index).reshape(ranks_decreasing_indexes.shape)
        gs_genes_to_rank_indexes = _isin(ranks_decreasing_indexes, gs_genes_index)
        # print(gs_genes_to_rank_indexes)

        # Compute ECDF for signature genes
        signature_ecdf = ranks_sorted_decreasing * gs_genes_to_rank_indexes
        signature_ecdf = signature_ecdf / np.sum(signature_ecdf, axis=0)
        signature_ecdf = np.cumsum(signature_ecdf, axis=0)

        # Compute ECDF for the remaining gene
        non_signature_ecdf = ~gs_genes_to_rank_indexes / np.sum(
            ~gs_genes_to_rank_indexes, axis=0
        )
        non_signature_ecdf = np.cumsum(non_signature_ecdf, axis=0)

        # sum of the difference between ECDFs
        enrichment_score = np.sum(signature_ecdf - non_signature_ecdf, axis=0)

        results[gs_name] = enrichment_score

    return results
