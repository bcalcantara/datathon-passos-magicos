📊 Datathon 5 — Passos Mágicos

Projeto desenvolvido para o Datathon da Pós-Tech, com foco em análise exploratória, modelagem preditiva e geração de insights estratégicos a partir dos dados do programa Passos Mágicos (2022–2024).

⸻

🎯 Objetivo

Analisar os indicadores acadêmicos, emocionais e de engajamento dos alunos para:
	•	Identificar padrões de desempenho
	•	Avaliar relações entre indicadores
	•	Construir modelo preditivo de risco
	•	Investigar a efetividade do programa ao longo do tempo
	•	Gerar insights estratégicos para a organização

⸻

📂 Estrutura
	•	data/ — dados brutos e tratados
	•	notebooks/ — análises exploratórias e modelagem
	•	src/ — código reutilizável
	•	app/ — aplicação Streamlit (se aplicável)
	•	models/ — modelos treinados

⸻

📌 Indicadores analisados
	•	IDA — Desempenho Acadêmico
	•	IEG — Engajamento
	•	IAA — Autoavaliação
	•	IPS — Indicador Psicossocial
	•	IPP — Indicador de Performance
	•	IAN — Indicador de Defasagem
	•	IPV — Indicador de Ponto de Virada
	•	INDE — Índice Global de Desenvolvimento

⸻

💎 Classificação por Pedra (baseada no INDE)
	•	Quartzo: 2,405 a 5,506
	•	Ágata: 5,506 a 6,868
	•	Ametista: 6,868 a 8,230
	•	Topázio: 8,230 a 9,294

Essa segmentação foi utilizada para avaliar evolução e distribuição de desempenho.

⸻

🔎 Principais Resultados

📈 Evolução do Programa
	•	Crescimento da proporção de alunos em Topázio ao longo dos anos.
	•	Melhora gradual nas médias de INDE.
	•	Indícios de evolução estrutural do desempenho.

🔗 Relações Relevantes
	•	Engajamento (IEG) apresenta forte associação com desempenho acadêmico.
	•	INDE é altamente explicado por IDA e IEG.
	•	IPS apresenta relação positiva com desempenho, mas não isoladamente determinante.

⚠️ Modelo de Risco
	•	AUC ≈ 0,76 (após correção de vazamento).
	•	Modelo identifica melhor alunos sem risco do que alunos críticos.
	•	Oportunidade de melhoria no recall da classe de risco.

⸻

💡 Insights Estratégicos
	•	Engajamento é um dos principais motores de desempenho.
	•	A maioria dos alunos está concentrada em Ametista (potencial de aceleração).
	•	Há desalinhamento entre percepção (IAA) e desempenho real.
	•	Sistema de alerta precoce pode ser estruturado combinando IEG + IPS.

⸻

⚠️ Limitações
	•	Ausência de acompanhamento longitudinal explícito por aluno.
	•	IPP disponível apenas em 2023–2024.
	•	Correlação não implica causalidade.
	•	Possível efeito de coorte entre anos.

⸻

🛠 Tecnologias Utilizadas
	•	Python
	•	Pandas
	•	NumPy
	•	Matplotlib / Seaborn
	•	Scikit-learn
	•	Streamlit (se aplicável)

Como rodar
pip install -r requirements.txt
jupyter notebook