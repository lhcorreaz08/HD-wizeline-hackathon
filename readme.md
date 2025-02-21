# Harley-Davidson Maintenance Assistant

## Overview
Motorcycle maintenance manuals contain **a vast amount of information**, making it difficult for riders to quickly find answers to their questions. Often, users do not know **where to look** for the specific details they need. Additionally, **new service technicians** may lack familiarity with certain models, especially **older or less common motorcycles**. 

This AI-powered assistant is designed to solve these challenges by providing **quick and relevant** answers based on the manual, helping both riders and maintenance professionals efficiently access important information.
This is a **Proof of Concept (PoC)** developed for a **Hackathon**, aiming to provide **motorcycle maintenance assistance** using AI-powered insights.

The solution leverages **Google Gemini AI** to dynamically process user queries and determine whether to:
1. **Consult the motorcycle manual** for maintenance-related questions.
2. **Locate the nearest service center** if the query is related to servicing needs.

## Features
- Leverages **AI-powered tools** that allow for scalable integration of new functionalities.
- Uses **dynamic tool selection**, enabling seamless expansion with additional services based on **user data and motorcycle telemetry**.
- Provides **a highly personalized experience** by utilizing relevant application and vehicle insights.
- Uses **Natural Language Processing (NLP)** to determine query intent.
- Fetches relevant information from the **motorcycle manual**.
- Provides **mock service center locations** using interactive maps.
- Implements a **Streamlit-based UI** for easy interaction.

## Technologies Used
- **Python** (primary programming language)
- **Streamlit** (web interface)
- **Google Gemini AI** (Generative AI model for response generation)
- **Folium** (for rendering service center maps)
- **Google GenerativeAI SDK**

## Project Structure
This repository contains the following key files:
- **`app.py`**: Contains the core application logic, including AI-powered query processing and Streamlit-based UI.
- **`manual.txt`**: A sample motorcycle manual that is used as a reference for answering user queries.

## Getting Started
### Prerequisites
Ensure you have **Python 3.8+** installed.

### Setup
#### 1. Clone the repository
```sh
git@github.com:lhcorreaz08/HD-wizeline-hackathon.git
cd harley-ai-maintenance
```

#### 2. Install dependencies
```sh
pip install -r requirements.txt
```

#### 3. Set up Google Gemini API Key
You need an **API key** to use Google Gemini AI.

- Go to **Google AI Studio** ([https://aistudio.google.com/](https://aistudio.google.com/))
- Navigate to **API Keys** and generate one.
- Set it as an environment variable:
```sh
export GEMINI_API_KEY="your_api_key_here"
```

#### 4. Run the application
```sh
streamlit run app.py
```

## How It Works
1. **User enters a query** related to motorcycle maintenance.
2. **The AI model determines** if the query should:
   - Retrieve relevant information from the **motorcycle manual**.
   - Provide the location of a **service center** (mock data).
3. **The response is displayed** with either maintenance instructions or a **map of the nearest service center**.

### Examples: 

1. **Querying the Maintenance Manual** - The assistant extracts relevant details from the manual based on the user's question.
![image](https://github.com/user-attachments/assets/054ba8c2-4b86-49e7-ae06-283c5ebc0c2c)
2. **Understanding Dashboard Messages** - The system helps decode warning messages displayed on the motorcycle.
![image](https://github.com/user-attachments/assets/c57bc5d1-25b9-4eae-aa0a-3860adde24e5)
3. **Finding the Nearest Service Center** - When needed, the assistant provides the closest service location using map integration.
![image](https://github.com/user-attachments/assets/859aad06-f3a0-4f6a-a444-802fcdb2d289)


## Future Enhancements
- **Integrate real-time service center data** from Harley-Davidson API.
- **Improve AI query processing** with vector search for more accurate results.
- **Support multiple languages** for a global audience.

## Contributors
Developed as part of a Hackathon project. Contributions welcome!

## License
MIT License

