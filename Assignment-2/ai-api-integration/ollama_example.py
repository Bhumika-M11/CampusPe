import requests

def ollama_query(prompt):
    try:
        response=requests.post(
            "http://localhost:11434/api/generate",
            json={"model":"llama3","prompt":prompt,"stream":False}
        )
        return response.json()["response"]
    except Exception as e:
        return f"Error:{e}"
    
if __name__=="__main__":
    prompt=input("Enter prompt:")
    print(ollama_query)