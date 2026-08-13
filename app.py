import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ========== CONFIGURAÇÃO DA PÁGINA ==========
st.set_page_config(page_title="Animes & Séries 🎬", layout="wide")

# ========== TÍTULO ==========
st.title("🎬 Ciência de Dados Pop: Animes & Séries")
st.markdown("Explore dados de seus animes e séries favoritas!")

# ========== CARREGAR DADOS ==========
df = pd.read_csv('dataset.csv')

# ========== FILTRO NO SIDEBAR ==========
genero_selecionado = st.sidebar.selectbox(
    "Escolha o Gênero:",
    ["Todos"] + df['Genero'].unique().tolist()
)



# ========== FILTRAR DADOS ==========
if genero_selecionado != "Todos":
    df_filtrado = df[df['Genero'] == genero_selecionado]
else:
    df_filtrado = df

# ========== MOSTRAR TABELA ==========
st.subheader("📊 Tabela de Dados")
st.dataframe(df_filtrado, use_container_width=True)

# ========== GRÁFICO DE BARRAS ==========
st.subheader("⭐ Nota IMDB por Título")
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(df_filtrado['Nome'], df_filtrado['Nota_IMDB'], color='#FF6B9D')
ax.set_xlabel("Título", fontsize=12)
ax.set_ylabel("Nota IMDB", fontsize=12)
ax.set_ylim(0, 10)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
st.pyplot(fig)

# ========== ESTATÍSTICAS ==========
st.subheader("📈 Estatísticas")
col1, col2, col3 = st.columns(3)
col1.metric("Média de Nota", f"{df_filtrado['Nota_IMDB'].mean():.2f}")
col2.metric("Nota Máxima", f"{df_filtrado['Nota_IMDB'].max():.1f}")
col3.metric("Total de Títulos", len(df_filtrado))
