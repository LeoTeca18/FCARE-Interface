💳 FCACRE - Sistema de Detecção de Fraudes em Cartões de Crédito

Interface da aplicação FCARE desenvolvida em Python + Streamlit para análise e detecção de fraudes em transações de cartão de crédito.
O sistema permite carregar datasets, visualizar dashboards e analisar transações em detalhes.

⚙️ Pré-requisitos

Antes de rodar a aplicação, é necessário ter instalado:

Python 3.9+

pip

📦 Instalação

Clone este repositório e entre na pasta do projeto:

git clone https://github.com/LeoTeca18/FCARE-Interface.git
cd FCARE-Interface


Crie um ambiente virtual e instale as dependências:

python -m venv venv

source venv/bin/activate   # Linux/Mac

venv\Scripts\activate      # Windows

pip install -r requirements.txt

▶️ Como Rodar

Execute o seguinte comando para iniciar a aplicação:

streamlit run Home.py

A aplicação abrirá automaticamente no navegador em:
👉 http://localhost:8501

🖼️ Interfaces da Aplicação

🏠 Inicial (Home.py): Tela de boas-vindas

🏠 Carregamento: Carregamento do dataset

📊 Dashboard: Visualização de métricas e gráficos globais

🔎 Análise das Transações: Listagem e filtro de transações suspeitas

📑 Detalhes das Transações: Histórico por usuário e métricas personalizadas


📚 Tecnologias Utilizadas

Python

Streamlit

Pandas / NumPy

Matplotlib / Plotly /

