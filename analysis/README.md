# Rerun the analysis (TODO)

## Instalation

No requirements file, sorry.

Using python=3.9.15

Install numpy, pandas, tqdm, numba, lifelines, matplotlib, statsmodels (TODO).

---

2. Run **parse_datasets.py** from _analysis_ folder. Make sure you have enough RAM (at least 8 GB, 5GB free)

3. Run **calculate_ssGSEA_scores.py** from _analysis_ folder to calculate ssGSEA for each sample-geneset pair in all TCGA datasets.

4. Run **calculate_logrank_test.py** from _analysis_ folder to calculate logrank tests.

5. Run **km_plotting.py** from _analysis_ folder to plot KM plots and save them in the _figures/KM_plots_ folder.

