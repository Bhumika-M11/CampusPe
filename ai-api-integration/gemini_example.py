import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api=genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def gemini_query(prompt):
    try:
        response=api.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"Error:{e}"

if __name__=="__main__":
    prompt=input("Enter prompt:")
    print(gemini_query(prompt))