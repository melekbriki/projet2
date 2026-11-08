"""Interface Streamlit. Lancer : streamlit run app.py"""
import pandas as pd
import streamlit as st

from sentiment import analyze, analyze_many

EMOJI = {"positive": "😀", "negative": "😠", "neutral": "😐"}

st.set_page_config(page_title="Sentiment Analysis", page_icon="💬")
st.title("💬 Analyse de sentiment (LangChain)")
provider = st.sidebar.selectbox("Fournisseur LLM", ["groq", "gemini"])

tab1, tab2 = st.tabs(["Un texte", "Plusieurs avis (un par ligne)"])

with tab1:
    text = st.text_area("Votre avis / commentaire", height=120)
    if st.button("Analyser", key="one") and text.strip():
        try:
            r = analyze(text, provider)
            st.subheader(f"{EMOJI[r.sentiment]} {r.sentiment.upper()}")
            st.progress(r.confidence, text=f"Confiance : {r.confidence:.0%}")
            st.info(r.reason)
        except Exception as e:
            st.error(f"Erreur : {e}")

with tab2:
    many = st.text_area("Un avis par ligne", height=200, key="many")
    if st.button("Analyser tout", key="batch"):
        lines = [l.strip() for l in many.splitlines() if l.strip()]
        if lines:
            try:
                res = analyze_many(lines, provider)
                df = pd.DataFrame(
                    {
                        "texte": lines,
                        "sentiment": [r.sentiment for r in res],
                        "confiance": [round(r.confidence, 2) for r in res],
                        "raison": [r.reason for r in res],
                    }
                )
                st.dataframe(df, use_container_width=True)
                st.bar_chart(df["sentiment"].value_counts())
            except Exception as e:
                st.error(f"Erreur : {e}")
