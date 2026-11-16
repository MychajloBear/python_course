import streamlit as st
import seaborn as sns


st.set_page_config(page_title="Statistik")

@st.cache_data
def load_data():
    return sns.load_dataset("penguins").dropna()

df=load_data()
st.title("📊 Statistik")

c1,c2,c3=st.columns(3)
c1.metric('Mittelwert',f"{df['body_mass_g'].mean():.0f} g")
c2.metric('Median',f"{df['body_mass_g'].median():.0f} g")
c3.metric('Standardabweichung',f"{df['body_mass_g'].std():.0f} g")

st.dataframe(df.describe())
