import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


def draw_heatmap(df: pd.DataFrame, cols: list[str]) -> None:
    """
    Draws a heatmap of the correlation matrix of the given DataFrame.

    Args:
        df (pd.DataFrame): The input DataFrame.
        cols (list[str]): The columns to include in the heatmap.
    """
    style = 'poster'
    color = 'Blues'
    fig_width = 30
    fig_height = 15
    linewidth = .5
    fmt = '.2f'
    
    sns.set_context(style)
    df_pick = df.loc[:, cols]
    fig, ax = plt.subplots(figsize=(fig_width, fig_height))
    sns.heatmap(
        df_pick.corr(),
        annot=True,
        fmt=fmt,
        linewidths=linewidth,
        cmap=color,
        ax=ax
    )
    st.pyplot(fig)
    