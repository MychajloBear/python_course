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



plt.style.use('seaborn-v0_8-whitegrid')
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.2), dpi=150)

# --- Сценарій 1: Дискретний розподіл (0 та 10 хв з рівною ймовірністю) ---
x1 = np.array([0, 10])
p1 = np.array([0.5, 0.5])

# Обчислення середнього за формулою математичного сподівання: μ = sum(x * P(x))
mu1 = np.sum(x1 * p1)
# Обчислення дисперсии та стандартного відхилення за формулою
var1 = np.sum(((x1 - mu1) ** 2) * p1)
std1 = np.sqrt(var1)

bars = ax1.bar(x1, p1, width=1.2, color='#2B5B84', edgecolor='black', alpha=0.85, label='Ймовірність $P(X = x)$')
ax1.axvline(mu1, color='#D9534F', linestyle='--', linewidth=2, label=f'Середнє $\\mu = {mu1:.1f}$ хв')
ax1.axvspan(mu1 - std1, mu1 + std1, color='#D9534F', alpha=0.12, label=f'$\\mu \\pm \\sigma$ ($[{mu1-std1:.0f}; {mu1+std1:.0f}]$ хв)')

ax1.set_title(f'Випадок 1: Дискретний розподіл (0 або 10 хв)\n$Var(X) = {var1:.0f}$ хв$^2$ ($\\sigma = {std1:.0f}$ хв)', fontweight='bold')
ax1.set_xlabel('Запізнення автобуса $X$ (хв)')
ax1.set_ylabel('Ймовірність $P(X = x)$ (сума = 1.0)')
ax1.set_xlim(-1.5, 11.5)
ax1.set_ylim(0, 0.65)
ax1.legend(loc='upper center')


# --- Сценарій 2: Неперервний рівномірний розподіл U(a, b) ---
a, b = 0, 10
x2 = np.linspace(-1.5, 11.5, 500)
y2 = np.where((x2 >= a) & (x2 <= b), 1 / (b - a), 0.0)

# Обчислення середнього за формулою рівномірного розподілу: μ = (a + b) / 2
mu2 = (a + b) / 2
# Обчислення дисперсії за формулою: Var(X) = (b - a)^2 / 12
var2 = ((b - a) ** 2) / 12
std2 = np.sqrt(var2)

ax2.plot(x2, y2, color='#2E8B57', linewidth=2.5, label=f'Щільність $f(x) = {1/(b-a)}$')
ax2.fill_between(x2, y2, color='#2E8B57', alpha=0.25)
ax2.axvline(mu2, color='#D9534F', linestyle='--', linewidth=2, label=f'Середнє $\\mu = {mu2:.1f}$ хв')
ax2.axvspan(mu2 - std2, mu2 + std2, color='#D9534F', alpha=0.12, label=f'$\\mu \\pm \\sigma$ ($[{mu2-std2:.2f}; {mu2+std2:.2f}]$ хв)')

ax2.text(5, 0.105, 'Площа = 1.0 (100%)', ha='center', va='bottom', fontsize=10, color='#1E5631', fontweight='bold')

ax2.set_title(f'Випадок 2: Неперервний рівномірний $U({a}, {b})$\n$Var(X) \\approx {var2:.2f}$ хв$^2$ ($\\sigma \\approx {std2:.2f}$ хв)', fontweight='bold')
ax2.set_xlabel('Запізнення автобуса $X$ (хв)')
ax2.set_ylabel('Щільність ймовірності $f(x)$ (площа = 1.0)')
ax2.set_xlim(-1.5, 11.5)
ax2.set_ylim(0, 0.14)
ax2.legend(loc='upper right')

plt.tight_layout()
plt.show()