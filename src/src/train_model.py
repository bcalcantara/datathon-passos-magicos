from pathlib import Path
import pandas as pd
import joblib
from modelo_risco import treinar_modelo

BASE_DIR = Path(__file__).resolve().parents[2]

caminho_dados = BASE_DIR / "data" / "processed" / "dados_tratados.csv"
caminho_modelo = BASE_DIR / "models" / "modelo_risco.pkl"

df = pd.read_csv(caminho_dados)

modelo = treinar_modelo(df)

joblib.dump(modelo, caminho_modelo)

print("Modelo salvo com sucesso!")