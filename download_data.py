"""
Script for downloading data from:
https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE62944

and storing relevant files into data/ folder.
"""
import os
import urllib.request


EXPRESSION_DATA_NAME = "GSM1536837_06_01_15_TCGA_24.tumor_Rsubread_TPM.txt.gz"
CLINICAL_DATA_NAME = (
    "GSE62944_06_01_15_TCGA_24_548_Clinical_Variables_9264_Samples.txt.gz"
)
CANCER_DATA_NAME = "GSE62944_06_01_15_TCGA_24_CancerType_Samples.txt.gz"


EXPRESSION_DATA_LINK = "https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSM1536837&format=file&file=GSM1536837%5F06%5F01%5F15%5FTCGA%5F24%2Etumor%5FRsubread%5FTPM%2Etxt%2Egz"

CLINICAL_DOWNLOAD_LINK = "https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE62944&format=file&file=GSE62944%5F06%5F01%5F15%5FTCGA%5F24%5F548%5FClinical%5FVariables%5F9264%5FSamples%2Etxt%2Egz"

CANCER_DOWNLOAD_LINK = "https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE62944&format=file&file=GSE62944%5F06%5F01%5F15%5FTCGA%5F24%5FCancerType%5FSamples%2Etxt%2Egz"


def download_expression_data() -> None:
    """
    PLEASE download the expression file manually.
    """

    if EXPRESSION_DATA_NAME in os.listdir("data"):
        print("Expression data already downloaded.")

    else:
        print(
            f"""
Expression data not found.
Please follow the instruction to download the expression data manually.

1.) Visit: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM1536837
2.) At the bottom of the page download GSM1536837_06_01_15_TCGA_24.tumor_Rsubread_TPM.txt.gz
3.) Move the downloaded file into the data/ folder.
"""
        )


def download_clinical_data() -> None:
    """
    Downloads TCGA clinical data from:
    https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE62944&format=file&file=GSE62944%5F06%5F01%5F15%5FTCGA%5F24%5F548%5FClinical%5FVariables%5F9264%5FSamples%2Etxt%2Egz
    """

    if CLINICAL_DATA_NAME in os.listdir("data"):
        print("Clinical data already downloaded.")

    else:
        urllib.request.urlretrieve(CLINICAL_DOWNLOAD_LINK, f"data/{CLINICAL_DATA_NAME}")


def download_cancer_data() -> None:
    """
    Downloads TCGA cancer information from:
    https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE62944&format=file&file=GSE62944%5F06%5F01%5F15%5FTCGA%5F24%5F548%5FClinical%5FVariables%5F9264%5FSamples%2Etxt%2Egz
    """

    if CANCER_DATA_NAME in os.listdir("data"):
        print("Cancer data already downloaded.")

    else:
        urllib.request.urlretrieve(CANCER_DOWNLOAD_LINK, f"data/{CANCER_DATA_NAME}")


if __name__ == "__main__":

    download_expression_data()

    download_clinical_data()

    download_cancer_data()
