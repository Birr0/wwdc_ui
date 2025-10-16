from pathlib import Path

import streamlit as st


ROOT = Path(__file__).resolve().parent.parent
IMAGE_DIR =  ROOT / "static" / "images"

st.set_page_config(layout="wide")

st.title("WWDC UI • Documentation")

tab1, tab2, tab3, tab4, tab5 = st.tabs(["WWDC*", "Getting Started", "Changing Plots", "Selecting Data", "Anomaly Inspection"])

with tab1:
    st.subheader("Introduction")
    st.image(str(ROOT / "static" / "WWDC_art.png"), caption="What We Don't Capture: artwork by Alicia Hayden.", width=1024)
    st.markdown(
    """
    **WWDC UI** provides an interface for interacting with embeddings produced by What We Don't C*. 
    What We Don't C* attempts to remove information already known about embeddings to produce novel representations
    which one can explore. It hoped that this system produces embeddings that are:
    - Useful
    - Informative
    - Interpretable

    Most importantly, details that are missed using the information already known about the object being represented 
    should present itself more clearly than the embedding space produced by a VAE.
    """
    )

with tab2:
    st.subheader("Getting started")
    st.markdown(
    """
    Under the WWDC embedding view or VAE embedding view, you will be presented with a dashboard that looks like the following:
    """
    )
    st.image(str(ROOT / "static" / "docs" / "atlas_panel.png"), caption="Embedding-Atlas Panel starting view.", width=1024)
    st.markdown(
    """
    A number of features come to eye. Firstly, at the centre is a visualisation of the embeddings for the dataset. 
    Below is a table containing all the information concerning the objects; clicking on the object's row transports one to it's place in the embedding space.
    On the right is a series of plots for data and metadata of interest for the objects. Right now the interface looks rather plain but we can customise this to make 
    it more visually appealing and useful. Firstly, one can colour the representations by their attributes using the 'color' drop-down menu: 
    """
    )
    st.image(str(ROOT / "static" / "docs" / "colour_points.png"), caption="Colouring digits by their attributes reveals subtle structures in the embedding space.", width=1024)
    st.markdown(
    """
    We can also add images for inspection of the objects in the table and in the tooltip. Firstly, click the settings icon ⚙️ on the top right of the screen. 
    Then select image and change: 1) (default) to Markdown and 2) Badge to Full:
    """
    )
    st.image(str(ROOT / "static" / "docs" / "select_images.png"), caption="Adding images to the viewer in settings ⚙️.", width=1024)

with tab3:
    st.subheader("Changing Plots")
    st.markdown(
    """
    The plots contained in the right hand panel can be changed and customised according to one's preference (for reference: https://github.com/uwdata/mosaic).
    The example below shows how to change the digits to be represented as a histogram. This data can be subsequently filtered for fine-grained inspection of the embeddings.
    """
    )
    st.image(str(ROOT / "static" / "docs" / "edit_plots.png"), caption="Changing the default plot for the digit attribute.", width=1024)

with tab4:
    st.subheader("Selecting Data")
    st.markdown(
    """
    It is possible to select data for closer inspection. In fact there are a number of useful ways to do so. Using the plots on the right-hand panel,
    subsets of the data can be filtered according to their attributes. For example, one can select based on the digit type by 
    highlighting the column of sevens we just created using the histogram:
    """
    )
    st.image(str(ROOT / "static" / "docs" / "select_7.png"), caption="Selecting embeddings based on their class.", width=1024)
    
    st.markdown(
        """
        In addition, using the lasso and box tools placed on the bottom right-hand side of the embedding plot makes it possible to select a subset of data.
        This data will be filtered in both the main panel and in the table. For example, selecting a cluster of data points from the embeddings 
        for the sevens selected above shows a particular type of sevens: those with a bar.
        """
    )
    st.image(str(ROOT / "static" / "docs" / "lasso.png"), caption="Clustering sevens with the bar property using the lasso tool.", width=1024)

with tab5:
    st.subheader("Anomaly Inspection")
    st.markdown(
    """
    WWDC* provides log-likelihood scores for the embeddings; these can be used naturally as an outlier score. One can select these scores in the plots on the right and inspect the outliers. 
    Examples for outliers selected on the WWDC conditional log-likelihood scores is shown below. We also provide other scores for the unconditional (conditioning information left intact) and VAE manifolds.
    """
    )
    st.image(str(ROOT / "static" / "docs" / "anomaly_inspection.png"), caption="Inspecting outliers in the WWDC embedding space.", width=1024)
