import streamlit as st

from services.iris.dataset import IrisDataset
from components.heatmap import draw_heatmap

def render_page() -> None:
    st.title("Iris Dataset")
    
    dataset = IrisDataset()
    st.dataframe(dataset.df)
    
    draw_heatmap(dataset.df, ["SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm"])

    
    
if __name__ == "__main__":
    render_page()