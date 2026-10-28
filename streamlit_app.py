import streamlit as st
import requests

st.set_page_config(page_title="PDF Chatbot", layout="centered")
st.title("PDF Chatbot")
st.write("Sube un PDF y haz preguntas sobre su contenido.")

with st.sidebar:
    st.header("Ingestión")
    uploaded = st.file_uploader("Sube PDF", type="pdf")
    if uploaded and st.button("Ingestar"):
        files = {"file": (uploaded.name, uploaded.getvalue(), "application/pdf")}
        resp = requests.post("http://localhost:8000/ingest", files=files)
        st.write(resp.json())

question = st.text_input("Tu pregunta")
if st.button("Preguntar") and question:
    resp = requests.post("http://localhost:8000/ask", params={"question": question})
    data = resp.json()
    st.subheader("Respuesta")
    st.write(data.get("response", "Sin respuesta"))
    st.subheader("Fuentes")
    for s in data.get("sources", []):
        st.write(s)
