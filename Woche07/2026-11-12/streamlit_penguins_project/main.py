import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stats

st.set_page_config(page_title="Penguin Analyse", page_icon="🐧", layout="wide")

@st.cache_data
def load_data():
    return sns.load_dataset("penguins").dropna()

df = load_data()
st.title("🐧 Palmer Penguins Analyse")

if "merkliste" not in st.session_state:
    st.session_state.merkliste = []

with st.popover("⚙️ Filter"):
    species = st.multiselect("Pinguin-Art", sorted(df['species'].unique()), default=sorted(df['species'].unique()))
    mass_range = st.slider("Körpermasse (g)", int(df['body_mass_g'].min()), int(df['body_mass_g'].max()), (int(df['body_mass_g'].min()), int(df['body_mass_g'].max())))

filtered = df[df['species'].isin(species) & df['body_mass_g'].between(mass_range[0], mass_range[1])]

col1,col2=st.columns([3,1])
with col1:
    fig,ax=plt.subplots()
    sns.scatterplot(data=filtered,x='bill_length_mm',y='body_mass_g',hue='species',ax=ax)
    st.pyplot(fig)
with col2:
    st.metric('Datensätze',len(filtered))
    st.metric('Ø Gewicht',f"{filtered['body_mass_g'].mean():.0f} g")

sel=st.selectbox('Art auswählen',sorted(df['species'].unique()))
if st.button('Zur Merkliste hinzufügen') and sel not in st.session_state.merkliste:
    st.session_state.merkliste.append(sel)

st.write(st.session_state.merkliste)
if st.toggle('Rohdaten anzeigen'):
    st.dataframe(filtered)