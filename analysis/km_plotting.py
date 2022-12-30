import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from lifelines import KaplanMeierFitter

from statsmodels.stats.multitest import fdrcorrection


def make_folders():
    if "figures" not in os.listdir("./"):
        os.mkdir("figures")

    if "KM_plots" not in os.listdir("figures"):
        os.mkdir("figures/KM_plots")


def load_logrank_data() -> pd.DataFrame:
    logrank = pd.read_csv("TCGA/logrank-scores.tsv", sep="\t", index_col=[0])

    # apply FDR over columns!
    for tcga in logrank.columns:
        logrank[tcga] = fdrcorrection(logrank[tcga].values)[1]

    logrank.index = [" ".join(x.split("_")[1:]) for x in logrank.index.values]

    return logrank


def choose_scope_for_plotting(
    logrank: pd.DataFrame, TOP_N_GENESETS: int, p_THRESHOLD: float
) -> list:

    scale_significant = np.array(
        [logrank[tcga].nsmallest(5).values.max() for tcga in logrank.columns]
    )
    is_top5 = (logrank - scale_significant) <= 0
    is_sign = logrank < p_THRESHOLD
    is_significant = is_top5 * is_sign

    hallmark_list, tcga_list = np.where(is_significant == True)

    return hallmark_list, tcga_list, is_significant


def plotting_km_plots(logrank, hallmark_list, tcga_list, is_significant):

    for geneset_id, tcga_id in zip(hallmark_list, tcga_list):

        geneset, tcga = (
            f"HALLMARK_{'_'.join(is_significant.index.values[geneset_id].split(' '))}",
            is_significant.columns[tcga_id],
        )
        print(geneset, tcga)

        ssGSEA = pd.read_csv(f"TCGA/TCGA-{tcga}-ssGSEA.tsv", sep="\t", index_col=[0])
        meta = pd.read_csv(f"TCGA/TCGA-{tcga}-metadata.tsv", sep="\t", index_col=[0])

        group = ssGSEA[geneset] > np.median(ssGSEA[geneset])
        group_names = ["down regulated", "up regulated"]  # for 0 and 1

        T = meta["time"]
        E = meta["event"]

        kmf = KaplanMeierFitter()
        plt.close("all")
        f, ax = plt.subplots(1, 1, figsize=(6, 4))

        kmf.fit(T[-group], event_observed=E[-group], label=group_names[0])
        kmf.plot_survival_function(ax=ax)

        kmf.fit(T[group], event_observed=E[group], label=group_names[1])
        kmf.plot_survival_function(ax=ax)

        ax.set_ylim(-0.2, 1.2)

        ax.set_title(
            f"TCGA {tcga} // {geneset} \n p-value: {logrank.iloc[geneset_id, tcga_id]:.3E}",
            fontsize=12,
        )

        f.savefig(
            f"figures/KM_plots/TCGA-{tcga}-{geneset}-KM.png",
            dpi=300,
            bbox_inches="tight",
        )


if __name__ == "__main__":

    # choose your own thresholds for plotting
    TOP_N_GENESETS = 5  # top significant pathways for each TCGA dataset
    p_THRESHOLD = 0.01  # p-value threshold for significance

    make_folders()

    logrank = load_logrank_data()

    hallmark_list, tcga_list, is_significant = choose_scope_for_plotting(
        logrank, TOP_N_GENESETS, p_THRESHOLD
    )

    plotting_km_plots(logrank, hallmark_list, tcga_list, is_significant)
