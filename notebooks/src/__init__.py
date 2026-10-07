requirements = f"""pandas
numpy
matplotlib
seaborn
biopython
mermaid-py
ipywidgets
google-drive
ipysheet
ipydatagrid
shinywidgets
altair
bokeh
plotly 
ipyleaflet 
pydeck==0.8.0
jupyterlite-pyodide-kernel
jupyter-book>=2.0
jupyter_server
"""

with open("./requirements.txt", "w") as f:
    f.write(requirements)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import seaborn as sns
from Bio import Entrez, Medline
import mermaid
import ipywidgets as widgets
from IPython.display import display, HTML, Javascript
import subprocess, sys, os, ssl, certifi
import re
from pathlib import Path

import os 
from pathlib import Path
root = os.getcwd()
folders = {
    "systematic_review": f"{root}/systematic_review",
        "protocol": f"{root}/systematic_review/protocol",
            "prospero": f"{root}/systematic_review/protocol/prospero",
            "cochrane": f"{root}/systematic_review/protocol/cochrane",
        "search_strategy": f"{root}/systematic_review/search_strategy",
        "search": f"{root}/systematic_review/search",
        "deduplication": f"{root}/systematic_review/deduplication",
        "screening": f"{root}/systematic_review/screening",
            "title_abstract": f"{root}/systematic_review/screening/title_abstract_screening", 
            "pdf": f"{root}/systematic_review/screening/PDF",
            "full_text": f"{root}/systematic_review/screening/full_text_screening", 
    "data_collection": f"{root}/data_collection",
        "database": f"{root}/data_collection/database",
    "meta-analysis": f"{root}/meta-analysis",
    "manuscript": f"{root}/manuscript"
}

print(folders)
for x, y in folders.items():
    filename = f"{x}"
    path = Path(f"{y}")
    os.makedirs(path, exist_ok = True)
    globals()[filename] = pathimport os 
