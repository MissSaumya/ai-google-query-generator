import streamlit as st
import sys
import os

# This trick helps Python find the 'src' folder when running from the 'app' folder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.query_engine import SearchQueryGenerator

# 1. Page Configuration (The Tab Title & Icon)
st.set_page_config(
    page_title="AI Search Assistant",
    page_icon="🔍",
    layout="centered"
)

# 2. Title and Description
st.title("🔍 AI Google Query Generator")
st.markdown("Enter any topic, and the AI will generate **10 professional search queries** for you.")

# 3. Sidebar (For Instructions)
with st.sidebar:
    st.header("How to use")
    st.write("1. Make sure LM Studio is running (Port 1234).")
    st.write("2. Enter your messy thought or question.")
    st.write("3. Click 'Generate Queries'.")
    st.success("Connected to Local AI")

# 4. Initialize the Logic (The Brain)
# We use @st.cache_resource so we don't reload the connection on every click
@st.cache_resource
def get_engine():
    return SearchQueryGenerator()

engine = get_engine()

# 5. User Input Area
user_input = st.text_area("What do you want to find?", height=100, placeholder="e.g., I want to fix my bike tire but I don't have tools...")

# 6. The Button & Action
if st.button("Generate Search Queries", type="primary"):
    if not user_input.strip():
        st.error("Please enter some text first!")
    else:
        # Show a spinner while the AI thinks
        with st.spinner("Thinking... (Consulting Qwen)..."):
            try:
                # Call the backend
                result = engine.generate_queries(user_input)
                
                # Display Results
                st.subheader("✅ Suggested Queries")
                st.markdown("---")
                st.markdown(result) # This prints the AI's formatted output
                
            except Exception as e:
                st.error(f"An error occurred: {e}")