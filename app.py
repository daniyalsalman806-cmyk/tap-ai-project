import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="TAP AI")
st.title("🤖 TAP AI")

# Apni Gemini Key yahan dhyan se paste karein
GEMINI_API_KEY = "AIzaSyDkZAK9tYHDs-dkwZdLGrp2BWcp6H7umn8"

genai.configure(api_key=GEMINI_API_KEY)

# Model ka naam 'gemini-1.5-pro' kar diya hai
model = genai.GenerativeModel('gemini-1.5-pro')

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("TAP se kuch puchein..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            response = model.generate_content(prompt)
            full_response = response.text
            st.markdown(full_response)
            st.session_state.messages.append({"role": "assistant", "content": full_response})
        except Exception as e:
            st.error(f"Error: {e}")
