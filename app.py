import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="ML Auto",
    page_icon="🧊",
    layout="wide",
)

# if 'ignore_col' not in st.session_state:
#     st.session_state.ignore_col = []


st.title('Auto ML Modelling')

ml_choice = ['Regression', 'Classification']

chosen_ml = st.selectbox('Choose the Model you wanna build', ml_choice)

st.write("Upload Your Dataset")
file = st.file_uploader("Choose your dataset to build ML")

if file: 
    df = pd.read_csv(file, index_col=None)
    st.dataframe(df, height=200)

    available_col = df.columns
    arr = []

    st.title('Data Preparation')

    chosen_target = st.selectbox('Choose the target column for your dataset', df.columns)

    col1, col2 = st.columns(2)

    with col1:
        ignore_cols = st.multiselect('Choose column to ignore for ML building',df.columns)
        st.write(ignore_cols)
    with col2:
        cat_cols = st.multiselect('Choose categorical column for ML building',df.columns)
        st.write(cat_cols)

    st.title('Model Benchmarking')


