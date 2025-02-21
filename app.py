import os
import google.generativeai as genai
import streamlit as st
import folium
from streamlit_folium import st_folium

# Configure API Key for Gemini
os.environ["GEMINI_API_KEY"] = "your_api_key_here"
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Model Configuration
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash-001",
  generation_config=generation_config,
)

chat_session = model.start_chat(history=[])

# Load the manual text file
with open("manual.txt", "r", encoding="ISO-8859-1") as file:
    manual_content = file.read()

# Streamlit Interface
st.set_page_config(page_title="Harley-Davidson Maintenance Assistant", page_icon="🏍️", layout="centered")

# Display Harley-Davidson Logo
st.image("harley_logo.png", width=150)

# Title and Description
st.title("Harley-Davidson Maintenance Assistant")
st.markdown("<h4 style='color: #FF6600;'>Proof of Concept for Hackathon</h4>", unsafe_allow_html=True)
st.markdown("<h4 style='color: #FF6600;'>Get maintenance information from your motorcycle manual.</h4>", unsafe_allow_html=True)

query = st.text_input("Ask a maintenance question about your motorcycle:")

# Ensure consistent UI updates by using session state
if "response" not in st.session_state:
    st.session_state.response = ""
if "map" not in st.session_state:
    st.session_state.map = None

# Function to determine tool usage dynamically using LLM
def select_tool_llm(question):
    system_prompt = "You are an AI assistant that determines whether a question is related to motorcycle maintenance (manual-based answer) or if it requires finding a service location. Respond with either 'manual' or 'service_locator'."
    classification_response = chat_session.send_message(f"{system_prompt}\n\nUser question: {question}\n\nAnswer with 'manual' or 'service_locator' only.")
    tool_selection = classification_response.text.strip().lower()
    return tool_selection if tool_selection in ["manual", "service_locator"] else "manual"

if st.button("Consult"):
    if query:
        tool = select_tool_llm(query)
        st.write(f"**Status:** {'Consulting Manual User' if tool == 'manual' else 'Locating Service Store'}")  # Debugging output to verify tool selection
        if tool == "manual":
            response = chat_session.send_message(f"Use the following motorcycle manual as a reference:\n\n{manual_content}\n\nAnswer the user's question accurately and provide relevant details:\n{query}")
            st.session_state.response = response.text
            st.session_state.map = None
        elif tool == "service_locator":
            st.session_state.response = "### Nearest Service Center (Mock Data):"
            m = folium.Map(location=[37.7749, -122.4194], zoom_start=10)
            folium.Marker([37.7749, -122.4194], popup="Harley-Davidson Service Center", tooltip="Click for details").add_to(m)
            st.session_state.map = m

# Display stored response or map
if st.session_state.response:
    st.write(st.session_state.response)
if st.session_state.map:
    st_folium(st.session_state.map, width=700, height=500)
