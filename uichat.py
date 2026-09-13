import streamlit as st
from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage
from dotenv import load_dotenv

load_dotenv()

# Page configuration
st.set_page_config(
    page_title="Mood AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

# Model
llm=HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1",
    max_new_tokens=200
)

model=ChatHuggingFace(llm=llm)

# Title
st.title("🤖 Mood AI Chatbot")
st.write("Choose a mood and start chatting!")

# Mood selection
mood = st.radio(
    "Choose your AI Mood:",
    ["😡 Angry Mode", "😂 Funny Mode", "😢 Sad Mode"],
    horizontal=True
)

# System prompt based on mood
if mood == "😡 Angry Mode":
    mode = """
    You are an Angry AI agent.
    Respond in an angry, frustrated and sarcastic style,
    but do not use abusive or hateful language.
    """

elif mood == "😂 Funny Mode":
    mode = """
    You are a Funny AI agent.
    Respond with humor, jokes and a playful personality.
    """

else:
    mode = """
    You are a Sad AI agent.
    Respond in a sad, emotional and slightly melancholic style.
    """

# Store conversation
if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content=mode)
    ]

# Display previous messages
for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.write(msg.content)

    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant"):
            st.write(msg.content)

# Chat input
prompt = st.chat_input("Ask me anything...")

if prompt:

    # User message
    st.session_state.messages.append(
        HumanMessage(content=prompt)
    )

    with st.chat_message("user"):
        st.write(prompt)

    # AI response
    response = model.invoke(
        st.session_state.messages
    )

    st.session_state.messages.append(
        AIMessage(content=response.content)
    )

    with st.chat_message("assistant"):
        st.write(response.content)
