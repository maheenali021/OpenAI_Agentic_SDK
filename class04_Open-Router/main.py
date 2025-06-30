from openai import OpenAI
import os
from dotenv import load_dotenv
from agents import Agent,AsyncOpenAI,OpenAIChatCompletionsModel,RunConfig # type: ignore
import streamlit as st
load_dotenv()


openrouter_api_key = os.getenv("OPENROUTER_API_KEY")

#agent level configration 
client = AsyncOpenAI(
    api_key=openrouter_api_key,
    base_url="https://openrouter.ai/api/v1")

model = OpenAIChatCompletionsModel(
    model= "mistralai/mistral-small-3.2-24b-instruct:free",
    openai_client= client
) # type: ignore
config = RunConfig(
    model= model,
    model_provider=client, #type:ignore
    tracing_disabled=True
)

agent = Agent(
        name= "Smart Python Solutions for AI Challenges",
        instructions= """Welcome to CodeCrawler Coding Solution, your dedicated AI-powered assistant for all things 
        Python programming! Whether you're a beginner learning the basics or an experienced developer tackling 
        complex projects.
       
        YOUR EXPERTIES:
        - Python Development Scripting, OOP, and clean code architecture.
        - Web Frameworks  Django, Flask, FastAPI for backend and APIs.
        - Data Science & AI  Pandas, NumPy, Scikit-learn, TensorFlow, and NLP.
        - Automation & Scripting  Selenium, BeautifulSoup, and workflow optimization.
        - Database Integration  SQL, PostgreSQL, MongoDB, and ORMs.
        - Algorithms & Problem-Solving  LeetCode-style challenges and optimizations.
        - DevOps & Deployment  Docker, CI/CD, and cloud platforms (AWS/GCP)."""
    
    )

#css file path
css_path = os.path.join(os.path.dirname(__file__), "style.css")
try:
    with open(css_path, "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
except FileNotFoundError:
    st.warning("Custom CSS file not found. Using default styles.")
    
#title
st.title(" CodeCrawler 🐍🧠")
st.subheader("Your AI-Powered Python Coding Companion 👨‍💻")
if 'openai_client' not in st.session_state:
    st.session_state['openai_client'] = OpenAI(
        api_key=openrouter_api_key,
        base_url="https://openrouter.ai/api/v1")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
    
# Chat input
if prompt := st.chat_input("Enter your prompt"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
     # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
            
     # Display assistant response
    with st.chat_message("assistant"):
        response = st.write_stream(
            st.session_state['openai_client'].chat.completions.create(
                model='mistralai/mistral-small-3.2-24b-instruct:free',
                messages=[
                    {"role": m["role"], "content": m["content"]} 
                    for m in st.session_state.messages
                ],
                stream=True
            )
        )
    
    # Add assistant response to chat history
    st.session_state["messages"].append({"role": "assistant", "content": response})
  
   
   
   
   
   






