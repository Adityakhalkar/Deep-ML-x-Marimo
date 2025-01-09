# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo",
#     "wigglystuff==0.1.7",
#     "numpy==2.2.1",
# ]
# ///

import marimo

__generated_with = "0.10.9"
app = marimo.App(css_file="/Users/adityakhalkar/Library/Application Support/mtheme/themes/deepml.css")


@app.cell
def _():
    import numpy as np
    return np


if __name__ == "__main__":
    app.run()