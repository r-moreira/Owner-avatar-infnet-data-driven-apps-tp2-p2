# INFNET 
## TP 2 - Data Driven APPs
### Aluno: Rodrigo Moreira Avila

---
### Sobre o projeto:
Aplicação para resolver uma série de exercícios utilizando fastapi

### Estrutura do projeto:
```./README.md``` - Este arquivo.


```./notebooks/*``` - Contém o notebook com a resolução dos exercícios teóricos.

```rodrigo_avila_DR3_TP2_p2.pdf``` - PDF contendo os prints e exercícios escritos.

```./src/*``` - Contém o código fonte da aplicação com a resolução de todos os exercícios.

```./images/*``` - Contém os prints para os exercícios.

```./requirements.txt``` - Contém as dependências do projeto.


### Como rodar o projeto streamlit:
1. Configurando versão do python:
```bash
pyenv local 3.11.9
```

2. Crie um ambiente virtual:
```bash
python -m venv .venv
```

3. Ative o ambiente virtual:
```bash
source .venv/bin/activate
```

4. Instale as dependências:
```bash
pip install -r requirements.txt
```

5. Execute a aplicação:
```bashu
uvicorn src.app:app --reload  
```