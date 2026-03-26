import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()
api=InferenceClient(
    token=os.getenv("HUGGING_API_KEY")
)

def hf_query(prompt):
    try:
        response=api.chat_completion(
            model="HuggingFaceH4/zephyr-7b-beta",
            messages=[
                {"role":"user","content":prompt}
            ],
            max_token=100
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error:{e}"

if __name__=="__main__":
    prompt=input("Enter prompt:")
    print(hf_query(prompt))