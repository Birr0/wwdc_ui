from pathlib import Path

import streamlit as st
from embedding_atlas.streamlit import embedding_atlas
import pandas as pd


ROOT = Path(__file__).resolve().parent.parent
IMAGE_DIR =  ROOT / "static" / "images"
ATLAS_DF = ROOT / "atlas_df.csv"

st.set_page_config(layout="wide")

# 2) Cache loading the Arrow IPC *stream*
@st.cache_data(show_spinner=False)
def load_df() -> pd.DataFrame:
    return pd.read_csv(str(ATLAS_DF))

df = load_df()
df.rename(
    columns={
        "wwdc_projection_x": "projection_x",
        "wwdc_projection_y": "projection_y"
    },
    inplace=True
)

st.title("WWDC • Embedding View")


# 4) Use a stable key so the component doesn't remount when df identity changes
value = embedding_atlas(
    df,
    x="projection_x",
    y="projection_y",
    neighbors="neighbors",
    show_table=True,
    key="atlas",     # <- stable key
    labels="digit",
)
