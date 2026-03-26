import os
import cohere
from dotenv import load_dotenv

load_dotenv()
api=cohere.ClientV2(os.getenv("COHERE_API_KEY"))

def cohere_query(prompt):
    try:
        response=api.chat(
            model="cpmmand-a-03-2025",
            messages=[
                {"role":"user","content":prompt}
            ]
        )
        return  response.message.content[0].text
    except Exception as e:
        return f"Error:{e}"   

if __name__=="__main__":
    prompt=input("Enter prompt:")
    print(cohere_query(prompt))