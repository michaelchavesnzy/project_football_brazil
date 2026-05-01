from etl.ingest import run_ingest
from dotenv import load_dotenv
import streamlit as st

if __name__ == "__main__":
    
    load_dotenv()

    df_classificacao = run_ingest()

    st.set_page_config(
    page_title="Brasileirão",
    layout="wide")

    st.title("Tabela do Brasileirão")
    st.dataframe(df_classificacao)

    st.image(df_classificacao.loc[df_classificacao['posicao'] == 1]['link_escudo'].iloc[0], caption="Primeiro colocado do campeonato")


    















