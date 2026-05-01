import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="TAP AI")
st.title("🤖 TAP AI")

# Yahan apni OpenAI API key dalein
client = OpenAI(api_key="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")


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
full_response = response.choices.message.content
st.markdown(full_response)
st.session_state.messages.append({"role": "assistant", "content": full_response})
