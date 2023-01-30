[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7572950.svg)](https://doi.org/10.5281/zenodo.7572950)


# AIME-2023: Ranking of Cancer Survival-Related Gene Sets through Integration of Single-Sample Gene Set Enrichment and Survival Analysis


The scripts and data used to perform the analysis and generate the figures are available in this repository.

## Instalation

The code was tested on Ubuntu 20.04.4 LTS and MacOS 13.1. With python versions 3.9.15 and 3.10.8.

Follow these steps to prepare the environment:

- Clone the repository

```bash
git clone https://github.com/biolab/AIME-2023-paper.git
cd AIME-2023-paper
```

- Install the required packages

```bash
# using pip in a virtual environment
pip install -r requirements.txt

# using Conda
conda create --name <env_name> --file requirements.txt
conda activate <env_name>
```

---

## Generating the data:

1. Run **download_data.py**. You will have to download a 1.4 Gb file manually. Instructions will be printed when you run a scipt.

2. Run **parse_datasets.py**. Make sure you have enough RAM (at least 8 GB)

3. Run **calculate_ssGSEA_scores.py**. This will calculate ssGSEA for each sample-geneset pair in all TCGA datasets.

4. Run **calculate_logrank_test.py**. This will calculate logrank tests and store the results.

## Generating plots

First, generate all the data before attempting to plot.

In the folder **notebooks/** there are notebooks that reproduce all the code necessary to plot figures 1 to 3. Figures are stored in the **figures/** folder.

# [Figure 1: Kaplan-Meier survival curves for the best-performing gene set.](notebooks/1.0-figure1.ipynb)

<img src="figures/figure1.png" alt="drawing" width="600"/>

</br>
</br>

# [Figure 2: Testing the robustness of the method](notebooks/2.0-figure2.ipynb)

<img src="figures/figure2.png" alt="drawing" width="600"/>

</br>
</br>

# [Figure 3: Comparison of Km plots for 50% and 75% enriched](notebooks/3.0-figure3.ipynb)

<img src="figures/figure3.png" alt="drawing" width="600"/>

---

## Extended table of references for the top gene sets

| TCGA | Hallmark gene set         |                                                                                                                                                                                                                                                                                              References |
|:-----|:--------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
| CESC | UV_RESPONSE_DN            |                                                                                                                                                                                                                   \[[1](#ref-jackson2000e6)\] \[[2](#ref-gu2019cervical)\] \[[3](#ref-wallace2012hpv)\] |
|      | ANGIOGENESIS              | \[[4](#ref-yang2021constructe)\] \[[5](#ref-xiong2019comprehensive)\] \[[6](#ref-wiggins1995tumor)\] \[[7](#ref-abulafia1999angiogenesis)\] \[[8](#ref-wang2019formation)\] \[[9](#ref-utrera2010role)\] \[[10](#ref-nie202029)\] \[[11](#ref-cheng1999vascular)\] \[[12](#ref-tomao2014angiogenesis)\] |
|      | PROTEIN_SECRETION         |                                                                                                                                                                      \[[13](#ref-noordhuis2009expression)\] \[[14](#ref-iida2011egfr)\] \[[15](#ref-ueda2017prognostic)\] \[[16](#ref-medda2021human)\] |
|      |                           |                                                                                                                                                                                                                                                                                                         |
| HNSC | GLYCOLYSIS                |                                                                                                             \[[17](#ref-kumar2017regulation)\] \[[18](#ref-curry2013cancer)\] \[[19](#ref-kumar2018cancer)\] \[[20](#ref-li2017blockage)\] \[[21](#ref-wang2021prognostic)\] \[[22](#ref-chen2021six)\] |
|      | MTORC1_SIGNALING          |                                                                                                                                                                     \[[23](#ref-simpson2015targeting)\] \[[24](#ref-vander2015pi)\] \[[25](#ref-lui2013frequent)\] \[[26](#ref-ding2022comprehensive)\] |
|      | XENOBIOTIC_METABOLISM     |                                                                                                                                                                                                                                            \[[27](#ref-oyelakin2022ehf)\] \[[28](#ref-namani2018gene)\] |
|      |                           |                                                                                                                                                                                                                                                                                                         |
| KIRC | HEME_METABOLISM           |                                                                                 \[[29](#ref-deng2019nrf2)\] \[[30](#ref-zhong2022fech)\] \[[31](#ref-takemoto2022bach1)\] \[[32](#ref-wu2020eleven)\] \[[33](#ref-chang2021ferroptosis)\] \[[34](#ref-liu2021decreased)\] \[[35](#ref-frezza2011haem)\] |
|      | FATTY_ACID_METABOLISM     |                                                                                                              \[[36](#ref-zhang2022potential)\] \[[37](#ref-liu2022decreased)\] \[[38](#ref-zhao2019mrna)\] \[[39](#ref-horiguchi2008fatty)\] \[[40](#ref-yuan2020expression)\] \[[41](#ref-du2017hif)\] |
|      | ANDROGEN_RESPONSE         |                                                                                                                                                                                                                                  \[[42](#ref-zhao2016protective)\] \[[43](#ref-foersch2017prognostic)\] |
|      |                           |                                                                                                                                                                                                                                                                                                         |
| LGG  | EMT                       |                                                                                                                                                                                                                                     \[[44](#ref-tao2020genomics)\] \[[45](#ref-iwadate2016epithelial)\] |
|      | ANGIOGENESIS              |                                                                                               \[[46](#ref-zhang2018idh)\] \[[47](#ref-plate1995angiogenesis)\] \[[48](#ref-majchrzak2013markers)\] \[[49](#ref-sun2006neuronal)\] \[[50](#ref-nam2004expression)\] \[[51](#ref-qian2018radiogenomics)\] |
|      | COAGULATION               |                                                                                                                                                                                                                                       \[[52](#ref-rong2005pten)\] \[[53](#ref-navone2019significance)\] |
|      |                           |                                                                                                                                                                                                                                                                                                         |
| LUAD | MTORC1_SIGNALING          |                                                                                                                                                                                                                                   \[[54](#ref-marinov2007targeting)\] \[[55](#ref-cheng2014targeting)\] |
|      | HYPOXIA                   |                                                                                                                                     \[[56](#ref-salem2018targeting)\] \[[57](#ref-mo2020identification)\] \[[58](#ref-hung2009prognostic)\] \[[59](#ref-sun2020development)\] \[[60](#ref-chen201917)\] |
|      | GLYCOLYSIS                |                                                                                                                                                                                                                            \[[61](#ref-zhang2019identification)\] \[[62](#ref-smolle2020distribution)\] |
|      |                           |                                                                                                                                                                                                                                                                                                         |
| SKCM | INTERFERON_GAMMA_RESPONSE |                                                                                                                                                                                                           \[[63](#ref-alavi2018interferon)\] \[[64](#ref-tiffen2020ezh2)\] \[[65](#ref-kim2020immune)\] |
|      | INTERFERON_ALPHA_RESPONSE |                                                                                                                                                                                                                                \[[63](#ref-alavi2018interferon)\] \[[66](#ref-kirkwood1996interferon)\] |
|      |                           |                                                                                                                                                                                                                                                                                                         |

## References

<div id="refs" class="references csl-bib-body">

<div id="ref-jackson2000e6" class="csl-entry">

<span class="csl-left-margin">1. </span><span
class="csl-right-inline">Jackson, S., Storey, A.: E6 proteins from
diverse cutaneous HPV types inhibit apoptosis in response to UV damage.
Oncogene. 19, 592–598 (2000).</span>

</div>

<div id="ref-gu2019cervical" class="csl-entry">

<span class="csl-left-margin">2. </span><span
class="csl-right-inline">Gu, W., Sun, S., Kahn, A., Dacus, D., Wendel,
S.O., McMillan, N., Wallace, N.A.: Cervical cancer cell lines are
sensitive to sub-erythemal UV exposure. Gene. 688, 44–53 (2019).</span>

</div>

<div id="ref-wallace2012hpv" class="csl-entry">

<span class="csl-left-margin">3. </span><span
class="csl-right-inline">Wallace, N.A., Robinson, K., Howie, H.L.,
Galloway, D.A.: HPV 5 and 8 E6 abrogate ATR activity resulting in
increased persistence of UVB induced DNA damage. PLoS pathogens. 8,
e1002807 (2012).</span>

</div>

<div id="ref-yang2021constructe" class="csl-entry">

<span class="csl-left-margin">4. </span><span
class="csl-right-inline">Yang, Y., Li, Y., Qi, R., Zhang, L.: Constructe
a novel 5 hypoxia genes signature for cervical cancer. Cancer cell
international. 21, 1–15 (2021).</span>

</div>

<div id="ref-xiong2019comprehensive" class="csl-entry">

<span class="csl-left-margin">5. </span><span
class="csl-right-inline">Xiong, J., Guo, S., Bing, Z., Su, Y., Guo, L.:
A comprehensive RNA expression signature for cervical squamous cell
carcinoma prognosis. Frontiers in genetics. 9, 696 (2019).</span>

</div>

<div id="ref-wiggins1995tumor" class="csl-entry">

<span class="csl-left-margin">6. </span><span
class="csl-right-inline">Wiggins, D.L., Granai, C.O., Steinhoff, M.M.,
Calabresi, P.: Tumor angiogenesis as a prognostic factor in cervical
carcinoma. Gynecologic oncology. 56, 353–356 (1995).</span>

</div>

<div id="ref-abulafia1999angiogenesis" class="csl-entry">

<span class="csl-left-margin">7. </span><span
class="csl-right-inline">Abulafia, O., Triest, W.E., Sherer, D.M.:
Angiogenesis in malignancies of the female genital tract. Gynecologic
oncology. 72, 220–231 (1999).</span>

</div>

<div id="ref-wang2019formation" class="csl-entry">

<span class="csl-left-margin">8. </span><span
class="csl-right-inline">Wang, Q., Steger, A., Mahner, S., Jeschke, U.,
Heidegger, H.: The formation and therapeutic update of tumor-associated
macrophages in cervical cancer. International journal of molecular
sciences. 20, 3310 (2019).</span>

</div>

<div id="ref-utrera2010role" class="csl-entry">

<span class="csl-left-margin">9. </span><span
class="csl-right-inline">Utrera-Barillas, D., Castro-Manrreza, M.,
Castellanos, E., Gutiérrez-Rodrı́guez, M., Esparza, O.A.-R. de,
Garcı́a-Cebada, J., Velazquez, J.R., Flores-Reséndiz, D.,
Hernández-Hernández, D., Benı́tez-Bribiesca, L.: The role of macrophages
and mast cells in lymphangiogenesis and angiogenesis in cervical
carcinogenesis. Experimental and molecular pathology. 89, 190–196
(2010).</span>

</div>

<div id="ref-nie202029" class="csl-entry">

<span class="csl-left-margin">10. </span><span
class="csl-right-inline">Nie, H., Bu, F., Xu, J., Li, T., Huang, J.: 29
immune-related genes pairs signature predict the prognosis of cervical
cancer patients. Scientific Reports. 10, 1–16 (2020).</span>

</div>

<div id="ref-cheng1999vascular" class="csl-entry">

<span class="csl-left-margin">11. </span><span
class="csl-right-inline">Cheng, W.-F., Chen, C.-A., Lee, C.-N., Chen,
T.-M., Hsieh, F.-J., Hsieh, C.-Y.: Vascular endothelial growth factor in
cervical carcinoma. Obstetrics & Gynecology. 93, 761–765 (1999).</span>

</div>

<div id="ref-tomao2014angiogenesis" class="csl-entry">

<span class="csl-left-margin">12. </span><span
class="csl-right-inline">Tomao, F., Papa, A., Rossi, L., Zaccarelli, E.,
Caruso, D., Zoratto, F., Panici, P.B., Tomao, S.: Angiogenesis and
antiangiogenic agents in cervical cancer. OncoTargets and therapy. 7,
2237 (2014).</span>

</div>

<div id="ref-noordhuis2009expression" class="csl-entry">

<span class="csl-left-margin">13. </span><span
class="csl-right-inline">Noordhuis, M.G., Eijsink, J.J., Ten Hoor, K.A.,
Roossink, F., Hollema, H., Arts, H.J., Pras, E., Maduro, J.H., Reyners,
A.K., Bock, G.H. de, others: Expression of epidermal growth factor
receptor (EGFR) and activated EGFR predict poor response to (chemo)
radiation and survival in cervical CancerThe EGFR pathway in
advanced-stage cervical cancer. Clinical cancer research. 15, 7389–7397
(2009).</span>

</div>

<div id="ref-iida2011egfr" class="csl-entry">

<span class="csl-left-margin">14. </span><span
class="csl-right-inline">Iida, K., Nakayama, K., Rahman, M., Rahman, M.,
Ishikawa, M., Katagiri, A., Yeasmin, S., Otsuki, Y., Kobayashi, H.,
Nakayama, S., others: EGFR gene amplification is related to adverse
clinical outcomes in cervical squamous cell carcinoma, making the EGFR
pathway a novel therapeutic target. British journal of cancer. 105,
420–427 (2011).</span>

</div>

<div id="ref-ueda2017prognostic" class="csl-entry">

<span class="csl-left-margin">15. </span><span
class="csl-right-inline">Ueda, A., Takasawa, A., Akimoto, T., Takasawa,
K., Aoyama, T., Ino, Y., Nojima, M., Ono, Y., Murata, M., Osanai, M.,
others: Prognostic significance of the co-expression of EGFR and HER2 in
adenocarcinoma of the uterine cervix. PLoS One. 12, e0184123
(2017).</span>

</div>

<div id="ref-medda2021human" class="csl-entry">

<span class="csl-left-margin">16. </span><span
class="csl-right-inline">Medda, A., Duca, D., Chiocca, S.: Human
papillomavirus and cellular pathways: Hits and targets. Pathogens. 10,
262 (2021).</span>

</div>

<div id="ref-kumar2017regulation" class="csl-entry">

<span class="csl-left-margin">17. </span><span
class="csl-right-inline">Kumar, D.: Regulation of glycolysis in head and
neck squamous cell carcinoma. Postdoc journal: a journal of postdoctoral
research and postdoctoral affairs. 5, 14 (2017).</span>

</div>

<div id="ref-curry2013cancer" class="csl-entry">

<span class="csl-left-margin">18. </span><span
class="csl-right-inline">Curry, J.M., Tuluc, M., Whitaker-Menezes, D.,
Ames, J.A., Anantharaman, A., Butera, A., Leiby, B., Cognetti, D.,
Sotgia, F., Lisanti, M.P., others: Cancer metabolism, stemness and tumor
recurrence: MCT1 and MCT4 are functional biomarkers of metabolic
symbiosis in head and neck cancer. Cell cycle. 12, 1371–1384
(2013).</span>

</div>

<div id="ref-kumar2018cancer" class="csl-entry">

<span class="csl-left-margin">19. </span><span
class="csl-right-inline">Kumar, D., New, J., Vishwakarma, V., Joshi, R.,
Enders, J., Lin, F., Dasari, S., Gutierrez, W.R., Leef, G., Ponnurangam,
S., others: Cancer-associated fibroblasts drive glycolysis in a
targetable signaling loop implicated in head and neck squamous cell
carcinoma progression. Cancer research. 78, 3769–3782 (2018).</span>

</div>

<div id="ref-li2017blockage" class="csl-entry">

<span class="csl-left-margin">20. </span><span
class="csl-right-inline">Li, H.-M., Yang, J.-G., Liu, Z.-J., Wang,
W.-M., Yu, Z.-L., Ren, J.-G., Chen, G., Zhang, W., Jia, J.: Blockage of
glycolysis by targeting PFKFB3 suppresses tumor growth and metastasis in
head and neck squamous cell carcinoma. Journal of Experimental &
Clinical Cancer Research. 36, 1–12 (2017).</span>

</div>

<div id="ref-wang2021prognostic" class="csl-entry">

<span class="csl-left-margin">21. </span><span
class="csl-right-inline">Wang, Y., Li, Y., Jiang, L., Ren, X., Cheng,
B., Xia, J.: Prognostic value of glycolysis markers in head and neck
squamous cell carcinoma: A meta-analysis. Aging (Albany NY). 13, 7284
(2021).</span>

</div>

<div id="ref-chen2021six" class="csl-entry">

<span class="csl-left-margin">22. </span><span
class="csl-right-inline">Chen, L., He, X., Yi, S., Liu, G., Liu, Y.,
Ling, Y.: Six glycolysis-related genes as prognostic risk markers can
predict the prognosis of patients with head and neck squamous cell
carcinoma. BioMed Research International. 2021, (2021).</span>

</div>

<div id="ref-simpson2015targeting" class="csl-entry">

<span class="csl-left-margin">23. </span><span
class="csl-right-inline">Simpson, D.R., Mell, L.K., Cohen, E.E.:
Targeting the PI3K/AKT/mTOR pathway in squamous cell carcinoma of the
head and neck. Oral oncology. 51, 291–298 (2015).</span>

</div>

<div id="ref-vander2015pi" class="csl-entry">

<span class="csl-left-margin">24. </span><span
class="csl-right-inline">Vander Broek, R., Mohan, S., Eytan, D., Chen,
Z., Van Waes, C.: The PI 3 k/a kt/m TOR axis in head and neck cancer:
Functions, aberrations, cross-talk, and therapies. Oral diseases. 21,
815–825 (2015).</span>

</div>

<div id="ref-lui2013frequent" class="csl-entry">

<span class="csl-left-margin">25. </span><span
class="csl-right-inline">Lui, V.W., Hedberg, M.L., Li, H., Vangara,
B.S., Pendleton, K., Zeng, Y., Lu, Y., Zhang, Q., Du, Y., Gilbert, B.R.,
others: Frequent mutation of the PI3K pathway in head and neck cancer
defines predictive BiomarkersMutation of PI3K pathway in head and neck
cancer. Cancer discovery. 3, 761–769 (2013).</span>

</div>

<div id="ref-ding2022comprehensive" class="csl-entry">

<span class="csl-left-margin">26. </span><span
class="csl-right-inline">Ding, Z., Shen, H., Xu, K., Wu, Y., Wang, S.,
Yi, F., Wang, D., Liu, Y.: Comprehensive analysis of mTORC1 signaling
pathway–related genes in the prognosis of HNSCC and the response to
chemotherapy and immunotherapy. Frontiers in Molecular Biosciences. 9,
(2022).</span>

</div>

<div id="ref-oyelakin2022ehf" class="csl-entry">

<span class="csl-left-margin">27. </span><span
class="csl-right-inline">Oyelakin, A., Nayak, K.B., Glathar, A.R.,
Gluck, C., Wrynn, T., Tugores, A., Romano, R.-A., Sinha, S.: EHF is a
novel regulator of cellular redox metabolism and predicts patient
prognosis in HNSCC. NAR cancer. 4, zcac017 (2022).</span>

</div>

<div id="ref-namani2018gene" class="csl-entry">

<span class="csl-left-margin">28. </span><span
class="csl-right-inline">Namani, A., Rahaman, M., Chen, M., Tang, X.,
others: Gene-expression signature regulated by the KEAP1-NRF2-CUL3 axis
is associated with a poor prognosis in head and neck squamous cell
cancer. BMC cancer. 18, 1–11 (2018).</span>

</div>

<div id="ref-deng2019nrf2" class="csl-entry">

<span class="csl-left-margin">29. </span><span
class="csl-right-inline">Deng, Y., Wu, Y., Zhao, P., Weng, W., Ye, M.,
Sun, H., Xu, M., Wang, C.: The Nrf2/HO-1 axis can be a prognostic factor
in clear cell renal cell carcinoma. Cancer Management and Research. 11,
1221 (2019).</span>

</div>

<div id="ref-zhong2022fech" class="csl-entry">

<span class="csl-left-margin">30. </span><span
class="csl-right-inline">Zhong, G., Li, Q., Luo, Y., Liu, Y., Liu, D.,
Wang, T., others: FECH expression correlates with the prognosis and
tumor immune microenvironment in clear cell renal cell carcinoma.
Journal of Oncology. 2022, (2022).</span>

</div>

<div id="ref-takemoto2022bach1" class="csl-entry">

<span class="csl-left-margin">31. </span><span
class="csl-right-inline">Takemoto, K., Kobatake, K., Miura, K.,
Fukushima, T., Babasaki, T., Miyamoto, S., Sekino, Y., Kitano, H., Goto,
K., Ikeda, K., others: BACH1 promotes clear cell renal cell carcinoma
progression by upregulating oxidative stress-related tumorigenicity.
Cancer Science. (2022).</span>

</div>

<div id="ref-wu2020eleven" class="csl-entry">

<span class="csl-left-margin">32. </span><span
class="csl-right-inline">Wu, Y., Wei, X., Feng, H., Hu, B., Liu, B.,
Luan, Y., Ruan, Y., Liu, X., Liu, Z., Wang, S., others: An eleven
metabolic gene signature-based prognostic model for clear cell renal
cell carcinoma. Aging (Albany NY). 12, 23165 (2020).</span>

</div>

<div id="ref-chang2021ferroptosis" class="csl-entry">

<span class="csl-left-margin">33. </span><span
class="csl-right-inline">Chang, K., Yuan, C., Liu, X.:
Ferroptosis-related gene signature accurately predicts survival outcomes
in patients with clear-cell renal cell carcinoma. Frontiers in Oncology.
1432 (2021).</span>

</div>

<div id="ref-liu2021decreased" class="csl-entry">

<span class="csl-left-margin">34. </span><span
class="csl-right-inline">Liu, X., Zhang, W., Wang, H., Zhu, L., Xu, K.:
Decreased expression of ACADSB predicts poor prognosis in clear cell
renal cell carcinoma. Frontiers in oncology. 11, (2021).</span>

</div>

<div id="ref-frezza2011haem" class="csl-entry">

<span class="csl-left-margin">35. </span><span
class="csl-right-inline">Frezza, C., Zheng, L., Folger, O., Rajagopalan,
K.N., MacKenzie, E.D., Jerby, L., Micaroni, M., Chaneton, B., Adam, J.,
Hedley, A., others: Haem oxygenase is synthetically lethal with the
tumour suppressor fumarate hydratase. Nature. 477, 225–228
(2011).</span>

</div>

<div id="ref-zhang2022potential" class="csl-entry">

<span class="csl-left-margin">36. </span><span
class="csl-right-inline">Zhang, H., Zhang, D., Hu, X.: A potential fatty
acid metabolism-related gene signature for prognosis in clear cell renal
cell carcinoma. Cancers. 14, 4943 (2022).</span>

</div>

<div id="ref-liu2022decreased" class="csl-entry">

<span class="csl-left-margin">37. </span><span
class="csl-right-inline">Liu, X., Zhang, W., Wang, H., Zhu, L., Xu, K.:
Decreased expression of ACADSB predicts poor prognosis in clear cell
renal cell carcinoma. Frontiers in oncology. 11, 5748 (2022).</span>

</div>

<div id="ref-zhao2019mrna" class="csl-entry">

<span class="csl-left-margin">38. </span><span
class="csl-right-inline">Zhao, Z., Liu, Y., Liu, Q., Wu, F., Liu, X.,
Qu, H., Yuan, Y., Ge, J., Xu, Y., Wang, H.: The mRNA expression
signature and prognostic analysis of multiple fatty acid metabolic
enzymes in clear cell renal cell carcinoma. Journal of Cancer. 10, 6599
(2019).</span>

</div>

<div id="ref-horiguchi2008fatty" class="csl-entry">

<span class="csl-left-margin">39. </span><span
class="csl-right-inline">Horiguchi, A., Asano, T., Asano, T., Ito, K.,
Sumitomo, M., Hayakawa, M.: Fatty acid synthase over expression is an
indicator of tumor aggressiveness and poor prognosis in renal cell
carcinoma. The Journal of urology. 180, 1137–1140 (2008).</span>

</div>

<div id="ref-yuan2020expression" class="csl-entry">

<span class="csl-left-margin">40. </span><span
class="csl-right-inline">Yuan, Y., Yang, X., Li, Y., Liu, Q., Wu, F.,
Qu, H., Gao, H., Ge, J., Xu, Y., Wang, H., others: Expression and
prognostic significance of fatty acid synthase in clear cell renal cell
carcinoma. Pathology-Research and Practice. 216, 153227 (2020).</span>

</div>

<div id="ref-du2017hif" class="csl-entry">

<span class="csl-left-margin">41. </span><span
class="csl-right-inline">Du, W., Zhang, L., Brett-Morris, A., Aguila,
B., Kerner, J., Hoppel, C.L., Puchowicz, M., Serra, D., Herrero, L.,
Rini, B.I., others: HIF drives lipid deposition and cancer in ccRCC via
repression of fatty acid metabolism. Nature communications. 8, 1–12
(2017).</span>

</div>

<div id="ref-zhao2016protective" class="csl-entry">

<span class="csl-left-margin">42. </span><span
class="csl-right-inline">Zhao, H., Leppert, J.T., Peehl, D.M.: A
protective role for androgen receptor in clear cell renal cell carcinoma
based on mining TCGA data. PLoS One. 11, e0146505 (2016).</span>

</div>

<div id="ref-foersch2017prognostic" class="csl-entry">

<span class="csl-left-margin">43. </span><span
class="csl-right-inline">Foersch, S., Schindeldecker, M., Keith, M.,
Tagscherer, K.E., Fernandez, A., Stenzel, P.J., Pahernik, S.,
Hohenfellner, M., Schirmacher, P., Roth, W., others: Prognostic
relevance of androgen receptor expression in renal cell carcinomas.
Oncotarget. 8, 78545 (2017).</span>

</div>

<div id="ref-tao2020genomics" class="csl-entry">

<span class="csl-left-margin">44. </span><span
class="csl-right-inline">Tao, C., Huang, K., Shi, J., Hu, Q., Li, K.,
Zhu, X.: Genomics and prognosis analysis of epithelial-mesenchymal
transition in glioma. Frontiers in Oncology. 10, 183 (2020).</span>

</div>

<div id="ref-iwadate2016epithelial" class="csl-entry">

<span class="csl-left-margin">45. </span><span
class="csl-right-inline">Iwadate, Y.: Epithelial-mesenchymal transition
in glioblastoma progression. Oncology letters. 11, 1615–1620
(2016).</span>

</div>

<div id="ref-zhang2018idh" class="csl-entry">

<span class="csl-left-margin">46. </span><span
class="csl-right-inline">Zhang, L., He, L., Lugano, R., Roodakker, K.,
Bergqvist, M., Smits, A., Dimberg, A.: IDH mutation status is associated
with distinct vascular gene expression signatures in lower-grade
gliomas. Neuro-oncology. 20, 1505–1516 (2018).</span>

</div>

<div id="ref-plate1995angiogenesis" class="csl-entry">

<span class="csl-left-margin">47. </span><span
class="csl-right-inline">Plate, K.H., Risau, W.: Angiogenesis in
malignant gliomas. Glia. 15, 339–347 (1995).</span>

</div>

<div id="ref-majchrzak2013markers" class="csl-entry">

<span class="csl-left-margin">48. </span><span
class="csl-right-inline">Majchrzak, K., Kaspera, W., Szymaś, J.,
Bobek-Billewicz, B., Hebda, A., Majchrzak, H.: Markers of angiogenesis
(CD31, CD34, rCBV) and their prognostic value in low-grade gliomas.
Neurologia i neurochirurgia polska. 47, 325–331 (2013).</span>

</div>

<div id="ref-sun2006neuronal" class="csl-entry">

<span class="csl-left-margin">49. </span><span
class="csl-right-inline">Sun, L., Hui, A.-M., Su, Q., Vortmeyer, A.,
Kotliarov, Y., Pastorino, S., Passaniti, A., Menon, J., Walling, J.,
Bailey, R., others: Neuronal and glioma-derived stem cell factor induces
angiogenesis within the brain. Cancer cell. 9, 287–300 (2006).</span>

</div>

<div id="ref-nam2004expression" class="csl-entry">

<span class="csl-left-margin">50. </span><span
class="csl-right-inline">Nam, D.-H., Park, K., Suh, Y.L., Kim, J.-H.:
Expression of VEGF and brain specific angiogenesis inhibitor-1 in
glioblastoma: Prognostic significance. Oncology reports. 11, 863–869
(2004).</span>

</div>

<div id="ref-qian2018radiogenomics" class="csl-entry">

<span class="csl-left-margin">51. </span><span
class="csl-right-inline">Qian, Z., Li, Y., Sun, Z., Fan, X., Xu, K.,
Wang, K., Li, S., Zhang, Z., Jiang, T., Liu, X., others: Radiogenomics
of lower-grade gliomas: A radiomic signature as a biological surrogate
for survival prediction. Aging (Albany NY). 10, 2884 (2018).</span>

</div>

<div id="ref-rong2005pten" class="csl-entry">

<span class="csl-left-margin">52. </span><span
class="csl-right-inline">Rong, Y., Post, D.E., Pieper, R.O., Durden,
D.L., Van Meir, E.G., Brat, D.J.: PTEN and hypoxia regulate tissue
factor expression and plasma coagulation by glioblastoma. Cancer
research. 65, 1406–1413 (2005).</span>

</div>

<div id="ref-navone2019significance" class="csl-entry">

<span class="csl-left-margin">53. </span><span
class="csl-right-inline">Navone, S.E., Guarnaccia, L., Locatelli, M.,
Rampini, P., Caroli, M., La Verde, N., Gaudino, C., Bettinardi, N.,
Riboni, L., Marfia, G., others: Significance and prognostic value of the
coagulation profile in patients with glioblastoma: Implications for
personalized therapy. World neurosurgery. 121, e621–e629 (2019).</span>

</div>

<div id="ref-marinov2007targeting" class="csl-entry">

<span class="csl-left-margin">54. </span><span
class="csl-right-inline">Marinov, M., Fischer, B., Arcaro, A.: Targeting
mTOR signaling in lung cancer. Critical reviews in oncology/hematology.
63, 172–182 (2007).</span>

</div>

<div id="ref-cheng2014targeting" class="csl-entry">

<span class="csl-left-margin">55. </span><span
class="csl-right-inline">Cheng, H., Shcherba, M., Pendurti, G., Liang,
Y., Piperdi, B., Perez-Soler, R.: Targeting the PI3K/AKT/mTOR pathway:
Potential for lung cancer treatment. Lung cancer management. 3, 67–75
(2014).</span>

</div>

<div id="ref-salem2018targeting" class="csl-entry">

<span class="csl-left-margin">56. </span><span
class="csl-right-inline">Salem, A., Asselin, M.-C., Reymen, B., Jackson,
A., Lambin, P., West, C.M., O’Connor, J.P., Faivre-Finn, C.: Targeting
hypoxia to improve non–small cell lung cancer outcome. JNCI: Journal of
the National Cancer Institute. 110, 14–30 (2018).</span>

</div>

<div id="ref-mo2020identification" class="csl-entry">

<span class="csl-left-margin">57. </span><span
class="csl-right-inline">Mo, Z., Yu, L., Cao, Z., Hu, H., Luo, S.,
Zhang, S.: Identification of a hypoxia-associated signature for lung
adenocarcinoma. Frontiers in genetics. 11, 647 (2020).</span>

</div>

<div id="ref-hung2009prognostic" class="csl-entry">

<span class="csl-left-margin">58. </span><span
class="csl-right-inline">Hung, J.-J., Yang, M.-H., Hsu, H.-S., Hsu,
W.-H., Liu, J., Wu, K.: Prognostic significance of hypoxia-inducible
factor-1*α*, TWIST1 and snail expression in resectable non-small cell
lung cancer. Thorax. 64, 1082–1089 (2009).</span>

</div>

<div id="ref-sun2020development" class="csl-entry">

<span class="csl-left-margin">59. </span><span
class="csl-right-inline">Sun, J., Zhao, T., Zhao, D., Qi, X., Bao, X.,
Shi, R., Su, C.: Development and validation of a hypoxia-related gene
signature to predict overall survival in early-stage lung adenocarcinoma
patients. Therapeutic advances in medical oncology. 12, 1758835920937904
(2020).</span>

</div>

<div id="ref-chen201917" class="csl-entry">

<span class="csl-left-margin">60. </span><span
class="csl-right-inline">Chen, Y.-L., Zhang, Y., Wang, J., Chen, N.,
Fang, W., Zhong, J., Liu, Y., Qin, R., Yu, X., Sun, Z., others: A 17
gene panel for non-small-cell lung cancer prognosis identified through
integrative epigenomic-transcriptomic analyses of hypoxia-induced
epithelial–mesenchymal transition. Molecular oncology. 13, 1490–1502
(2019).</span>

</div>

<div id="ref-zhang2019identification" class="csl-entry">

<span class="csl-left-margin">61. </span><span
class="csl-right-inline">Zhang, L., Zhang, Z., Yu, Z.: Identification of
a novel glycolysis-related gene signature for predicting metastasis and
survival in patients with lung adenocarcinoma. Journal of translational
medicine. 17, 1–13 (2019).</span>

</div>

<div id="ref-smolle2020distribution" class="csl-entry">

<span class="csl-left-margin">62. </span><span
class="csl-right-inline">Smolle, E., Leko, P., Stacher-Priehse, E.,
Brcic, L., El-Heliebi, A., Hofmann, L., Quehenberger, F., Hrzenjak, A.,
Popper, H.H., Olschewski, H., others: Distribution and prognostic
significance of gluconeogenesis and glycolysis in lung cancer. Molecular
oncology. 14, 2853–2867 (2020).</span>

</div>

<div id="ref-alavi2018interferon" class="csl-entry">

<span class="csl-left-margin">63. </span><span
class="csl-right-inline">Alavi, S., Stewart, A.J., Kefford, R.F., Lim,
S.Y., Shklovskaya, E., Rizos, H.: Interferon signaling is frequently
downregulated in melanoma. Frontiers in immunology. 9, 1414
(2018).</span>

</div>

<div id="ref-tiffen2020ezh2" class="csl-entry">

<span class="csl-left-margin">64. </span><span
class="csl-right-inline">Tiffen, J., Gallagher, S.J., Filipp, F.,
Gunatilake, D., Al Emran, A., Cullinane, C., Dutton-Register, K., Aoude,
L., Hayward, N., Chatterjee, A., others: EZH2 cooperates with DNA
methylation to downregulate key tumor suppressors and IFN gene
signatures in melanoma. Journal of Investigative Dermatology. 140,
2442–2454 (2020).</span>

</div>

<div id="ref-kim2020immune" class="csl-entry">

<span class="csl-left-margin">65. </span><span
class="csl-right-inline">Kim, Y.-J., Kim, K., Lee, K.H., Kim, J., Jung,
W.: Immune expression signatures as candidate prognostic biomarkers of
age and gender survival differences in cutaneous melanoma. Scientific
reports. 10, 1–10 (2020).</span>

</div>

<div id="ref-kirkwood1996interferon" class="csl-entry">

<span class="csl-left-margin">66. </span><span
class="csl-right-inline">Kirkwood, J.M., Strawderman, M.H., Ernstoff,
M.S., Smith, T.J., Borden, E.C., Blum, R.H.: Interferon alfa-2b adjuvant
therapy of high-risk resected cutaneous melanoma: The eastern
cooperative oncology group trial EST 1684. Journal of clinical oncology.
14, 7–17 (1996).</span>

</div>

</div>
