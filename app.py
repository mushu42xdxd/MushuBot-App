import streamlit as st

API_KEY_VALIDA = "MUSHU42XD"

st.title("🧠 MushuBot con Key")
key_ingresada = st.text_input("Pon tu API Key pa entrar:", type="password")

if key_ingresada == API_KEY_VALIDA:
    st.success("🎉 Acceso autorizado. Bienvenido al Modo Mushu!")
    st.write("Aquí irán tus frases, botones y la gloriosa Caja -X 💀")
else:
    st.warning("🚫 Acceso denegado. Sin key no hay Mushu 😈")