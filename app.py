import streamlit as st
import pandas as pd
import json
from logic import get_insights

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
    
    st.subheader("Invencibilidade (Nunca perdeu para)")
    df_inv = pd.DataFrame(data["invincibility"])
    st.dataframe(df_inv, use_container_width=True)
    
    st.divider()
    
    st.subheader("Decks Mais Utilizados")
    df_used = pd.DataFrame(data["most_used_decks"])
    st.dataframe(df_used, use_container_width=True)