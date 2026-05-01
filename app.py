import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="TAP AI")
st.title("🤖 TAP AI")

# Apni API Key yahan sahi se dalein
client = OpenAI(api_key="sk-proj-TUzKwdK1Rx6WwXtExwBrUQHR9r_z0iKBM31NfRE2HCQdnfb9oW0l59ojAZPSJI50qBncCLi5xzT3B1bkFJA4Ms")

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
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Aapka naam TAP hai. Aap har baat ka sahi jawab dete hain."},
                *[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages]
            ]
        )
        full_response = response.choices[0].message.content
        st.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})
