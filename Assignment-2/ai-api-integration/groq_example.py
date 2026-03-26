import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
api=Groq(api_key=os.getenv("GROQ_API_KEY"))

def groq_query(prompt):
    try:
        response=api.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role":"user","content":prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error:{e}"

if __name__=="__main__":
    prompt=input("Enter prompt:")
    print(groq_query(prompt))