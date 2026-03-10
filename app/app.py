from pathlib import Path
import joblib
import pandas as pd
import streamlit as st

# caminhos
BASE_DIR = Path(__file__).resolve().parents[1]
caminho_modelo = BASE_DIR / "models" / "modelo_risco.pkl"

# carregar modelo
modelo = joblib.load(caminho_modelo)

# configuração da página
st.set_page_config(
    page_title="Previsão de Risco Escolar",
    page_icon="📊",
    layout="centered"
)

# título
st.title("📊 Previsão de Risco Escolar")
st.markdown(
    """
    Este aplicativo estima a **probabilidade de risco de queda no desempenho acadêmico**
    com base nos indicadores do aluno.

    **Variáveis utilizadas no modelo:**
    - IEG: Engajamento
    - IPP: Indicador Psicopedagógico
    - IPS: Indicador Psicossocial
    - IAA: Autoavaliação
    - IAN: Adequação / Defasagem
    """
)

st.divider()

# inputs
ieg = st.slider("IEG — Engajamento", min_value=0.0, max_value=10.0, value=5.0, step=0.1)
ipp = st.slider("IPP — Indicador Psicopedagógico", min_value=0.0, max_value=10.0, value=5.0, step=0.1)
ips = st.slider("IPS — Indicador Psicossocial", min_value=0.0, max_value=10.0, value=5.0, step=0.1)
iaa = st.slider("IAA — Autoavaliação", min_value=0.0, max_value=10.0, value=5.0, step=0.1)
ian = st.slider("IAN — Adequação / Defasagem", min_value=0.0, max_value=10.0, value=5.0, step=0.1)

st.divider()

# previsão
if st.button("Calcular probabilidade de risco"):
    entrada = pd.DataFrame([{
        "IEG": ieg,
        "IPP": ipp,
        "IPS": ips,
        "IAA": iaa,
        "IAN": ian
    }])

    prob_risco = modelo.predict_proba(entrada)[0][1]

    st.subheader("Resultado")
    st.metric("Probabilidade de risco", f"{prob_risco:.2%}")

    if prob_risco >= 0.70:
        st.error("⚠️ Alto risco de queda de desempenho.")
    elif prob_risco >= 0.40:
        st.warning("⚠️ Risco moderado de queda de desempenho.")
    else:
        st.success("✅ Baixo risco de queda de desempenho.")

    st.markdown("### Interpretação")
    st.write(
        """
        A previsão é baseada em um modelo de regressão logística treinado com dados históricos.
        O resultado representa uma **estimativa probabilística** e deve ser interpretado como apoio à decisão,
        não como diagnóstico definitivo.
        """
    )

st.divider()

# rodapé
st.caption("Modelo treinado a partir da análise do programa Passos Mágicos.")