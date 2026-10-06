from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

def page86_ai_msg():
    load_dotenv()
    llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.7)
    input_text=input("Enter text to translate: ")
    
    messages = [
        (
            "system", "당신은 사용자가 한 말을 영어로 번역하는 유능한 번역가 입니다.",
        ),
        (
            "human", input_text,
        ),
    ]
    
    ai_msg = llm.invoke(messages)
    
    print(f"AI Message: {ai_msg.text}")