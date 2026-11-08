# Projet 2 : Sentiment Analysis avec LangChain

## Objectif
Classer un texte (avis, commentaire) en **positive / negative / neutral**, avec un score de confiance et une explication.

## Installation
```powershell
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```
Créer un fichier `.env` (même que le projet 1) :
```
GROQ_API_KEY=ta_cle
GROQ_MODEL=openai/gpt-oss-20b
LLM_PROVIDER=groq
```

## Lancer
```powershell
python sentiment.py       # 10 tests + accuracy
streamlit run app.py      # interface web
```

## Architecture
`ChatPromptTemplate` -> `llm.with_structured_output(SentimentResult)` : le LLM renvoie un objet Pydantic validé (sentiment, confidence, reason).
`.batch()` traite plusieurs avis en parallèle.

## Limites et améliorations
- Sarcasme et négations : cas difficiles (voir tests 8 et 10) -> few-shot examples dans le prompt.
- Seulement 3 classes -> ajouter des émotions (joie, colère...) ou un score 1-5.
- Jeu de test petit (10 phrases) -> utiliser un vrai dataset (ex. avis clients) et calculer précision/rappel/F1.
- Sentiment par aspect (batterie vs écran) -> extraction par aspect avec un schéma plus riche.
- Dépend d'une API externe (quota, latence) -> modèle local (Ollama) ou modèle Hugging Face fine-tuné.
