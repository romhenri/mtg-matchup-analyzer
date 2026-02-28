import streamlit as st
import pandas as pd
import json
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from logic import get_insights

def get_color_with_alpha(val, alpha=0.5):
    if pd.isna(val):
        return ""
    cmap = plt.get_cmap("RdYlGn")
    norm = mcolors.Normalize(vmin=0, vmax=100)
    rgba = cmap(norm(val))
    
    darken_factor = 0.55
    r = int(rgba[0] * 255 * darken_factor)
    g = int(rgba[1] * 255 * darken_factor)
    b = int(rgba[2] * 255 * darken_factor)
    
    return f"background-color: rgba({r}, {g}, {b}, {alpha})"

st.set_page_config(page_title="Magic: The Gathering Insights", layout="wide")

st.title("Análise de Partidas de Magic")

uploaded_file = st.file_uploader("Faça upload do seu CSV", type=["csv"])

if uploaded_file is not None:
    json_data = get_insights(uploaded_file)
    data = json.loads(json_data)
    
    st.download_button(
        label="Baixar resultados em JSON",
        data=json_data,
        file_name="magic_insights.json",
        mime="application/json"
    )
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Confrontos Mais Comuns (x1)")
        df_common = pd.DataFrame(data["most_common_matchups"])
        st.dataframe(df_common, use_container_width=True)
        
    with col2:
        st.subheader("Confrontos que Nunca Aconteceram")
        df_never = pd.DataFrame(data["never_happened"])
        st.dataframe(df_never, use_container_width=True)
        
    st.divider()
    
    col3, col4 = st.columns(2)
    
    with col3:
        st.subheader("Taxa de Vitória (Win Rate)")
        df_wr = pd.DataFrame(data["win_rates"])
        
        styled_wr = df_wr.style.map(
            lambda v: get_color_with_alpha(v, alpha=0.2), 
            subset=["Win Rate (%)"]
        ).format({"Win Rate (%)": "{:.2f}%"})
        
        st.dataframe(styled_wr, use_container_width=True)
        
    with col4:
        st.subheader("Invencibilidade (Nunca perdeu para)")
        df_inv = pd.DataFrame(data["invincibility"])
        st.dataframe(df_inv, use_container_width=True)
    
    st.divider()
    
    st.subheader("Decks Mais Utilizados")
    df_used = pd.DataFrame(data["most_used_decks"])
    st.dataframe(df_used, use_container_width=True)