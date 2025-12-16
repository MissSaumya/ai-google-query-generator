import os
from openai import OpenAI
from dotenv import load_dotenv

# 1. Load the variables from the .env file
load_dotenv()

class SearchQueryGenerator:
    """
    A dedicated class to handle communication with the Local LLM (LM Studio).
    """
    
    def __init__(self):
        # 2. Initialize the Client using credentials from .env
        # We use os.getenv so we don't hardcode sensitive info
        self.client = OpenAI(
            base_url=os.getenv("LM_STUDIO_URL"),
            api_key=os.getenv("LM_STUDIO_KEY")
        )
        self.model = os.getenv("MODEL_NAME")

    def generate_queries(self, user_topic: str) -> str:
        """
        Sends the user's topic to the LLM and returns the generated queries.
        """
        
        # 3. The System Prompt (The Persona)
        system_instruction = (
            "You are an expert Search Engine Optimization (SEO) specialist. "
            "Your goal is to help users find the best information on Google "
            "by converting their raw ideas into professional search queries."
        )

        # 4. The User Prompt (The Task)
        # We ask for a specific format so it looks good on the frontend later.
        user_message = f"""
        User Input: "{user_topic}"

        Task:
        1. Identify the core intent of the user.
        2. Generate 10 distinct Google search queries.
        3. Provide a mix of broad searches and specific technical searches.

        Output Format:
        ### Analysis
        [One sentence analyzing the intent]

        ### Search Queries
        1. [Query 1]
        2. [Query 2]
        ...
        10. [Query 10]
        """

        try:
            print(f"DEBUG: Sending request to {self.model}...")
            
            # 5. Send to LM Studio
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_instruction},
                    {"role": "user", "content": user_message}
                ],
                temperature=0.7, # 0.7 = Creative but focused
            )
            
            # 6. Extract the text
            return response.choices[0].message.content

        except Exception as e:
            return f"Error connecting to LM Studio: {e}"