import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# =====================================
# CONFIGURAÇÃO DA PÁGINA
# =====================================

st.set_page_config(
    page_title="FarmTech Dashboard",
    page_icon="🌱",
    layout="wide"
)

# =====================================
# TÍTULO
# =====================================

st.title("🌱 FarmTech Solutions")
st.subheader("Dashboard de Irrigação Inteligente")

# =====================================
# LEITURA DO CSV
# =====================================

df = pd.read_csv("dados/sensores.csv")

# =====================================
# AJUSTANDO VALORES
# =====================================

df["umidade"] = pd.to_numeric(df["umidade"]) / 100
df["ph"] = pd.to_numeric(df["ph"]) / 100

# =====================================
# MÉTRICAS PRINCIPAIS
# =====================================

total_registros = len(df)

media_umidade = df["umidade"].mean()

media_ph = df["ph"].mean()

total_ligada = (df["status"] == "LIGADA").sum()

# =====================================
# KPIs
# =====================================

st.subheader("📌 Indicadores Gerais")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total de Registros", total_registros)

col2.metric("Média Umidade", f"{media_umidade:.2f}%")

col3.metric("Média pH", f"{media_ph:.2f}")

col4.metric("Irrigações Ligadas", total_ligada)

# =====================================
# STATUS DA IRRIGAÇÃO
# =====================================

st.subheader("🚰 Status da Irrigação")

status_counts = df["status"].value_counts()

fig, ax = plt.subplots()

ax.bar(status_counts.index, status_counts.values)

ax.set_ylabel("Quantidade")

st.pyplot(fig)

# =====================================
# MOTIVOS MAIS FREQUENTES
# =====================================

st.subheader("🧠 Motivos de Bloqueio da Irrigação")

motivos = df["motivo"].value_counts()

fig2, ax2 = plt.subplots()

ax2.bar(motivos.index, motivos.values)

ax2.set_ylabel("Quantidade")

plt.xticks(rotation=15)

st.pyplot(fig2)

# =====================================
# CONDIÇÃO CLIMÁTICA
# =====================================

st.subheader("🌦️ Sugestão Climática")

st.info(
    "Sem previsão de chuva: irrigação permitida.\n\n"
    "Com previsão de chuva: irrigação bloqueada para economia de água."
)

# =====================================
# STATUS DOS NUTRIENTES
# =====================================

st.subheader("🌱 Nutrientes NPK")

st.success("Sistema monitorando disponibilidade de Nitrogênio (N), Fósforo (P) e Potássio (K).")

# =====================================
# MÉDIA POR STATUS
# =====================================

st.subheader("📈 Média de Umidade e pH por Status")

media_status = df.groupby("status")[["umidade", "ph"]].mean()

st.dataframe(media_status)

# =====================================
# TABELA FINAL
# =====================================

st.subheader("📋 Dados Coletados")

st.dataframe(df)