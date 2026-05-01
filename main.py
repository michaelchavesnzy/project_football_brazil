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

    

    













