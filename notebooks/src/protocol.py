import ipywidgets as widgets
from IPython.display import display

picos = {
    "population/participation",
    "intervention",
    "comparator(s)",
    "outcome(s)",
    "study design"
}

for x in picos:
    return widgets.Text(description = f"{x}")
