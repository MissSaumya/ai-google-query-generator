# AI Smart Search Assistant (Local LLM)

## Project Overview
This project is an intelligent query expansion tool designed to convert raw user input into precise, optimized Google search queries. It utilizes a local Large Language Model (LLM) via LM Studio to perform intent analysis and keyword extraction, ensuring privacy and zero external API dependency.

The system is designed with a modular architecture, separating the backend logic (Python/OpenAI Client) from the frontend interface (Streamlit).

## Key Features
* **Intent Analysis:** Parses vague or unstructured user input to identify core search intent.
* **Local Inference:** Powered entirely by local models (e.g., Qwen 2.5) running on LM Studio.
* **Privacy Centric:** No data is transmitted to external cloud providers.
* **Modular Design:** Clean separation between the query engine and the user interface.

## Technical Architecture
* **Language:** Python 3.9+
* **Frontend:** Streamlit
* **Backend Communication:** OpenAI Client (configured for Local Host)
* **Model Server:** LM Studio

## Directory Structure
* `app/ui_main.py`: The entry point for the Streamlit web interface.
* `src/query_engine.py`: Encapsulates the logic for interacting with the local LLM.
* `requirements.txt`: List of Python dependencies.
* `.env`: Configuration file for environment variables (API keys and URLs).

## Setup and Installation

### 1. Prerequisites
Ensure the following are installed:
* Python 3.8 or higher
* LM Studio (with a model loaded and server running on port 1234)

### 2. Installation
Clone the repository and navigate to the project folder:
git clone https://github.com/YOUR_USERNAME/ai-google-query-generator.git
cd ai-google-query-generator

### 3. Environment Setup
Create a virtual environment to manage dependencies:

# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate

Install the required packages:
pip install -r requirements.txt

### 4. Configuration
Create a file named `.env` in the root directory with the following content:
LM_STUDIO_URL=http://localhost:1234/v1
LM_STUDIO_KEY=lm-studio
MODEL_NAME=local-model

## Usage
1.  Launch the LM Studio server.
2.  Run the application using Streamlit:
    streamlit run app/ui_main.py
3.  Access the interface at `http://localhost:8501` in your web browser.
