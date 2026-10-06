from dotenv import load_dotenv
from langgraph.graph import StateGraph
from langgraph.graph import START, END
from IPython.display import Image, display
from langchain_openai import ChatOpenAI
from typing import TypedDict, Annotated
from operator import add

from langgraph.graph import StateGraph
from pathlib import Path
from agent_one import app

load_dotenv()

class InputState(TypedDict):
    question: str

class OutputState(TypedDict):
    answer: str

class OverallState(TypedDict):
    messages: Annotated[list[str], add]
    question: str
    answer: str

llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.7)
def chatbot(state: InputState) -> OverallState:
    question = state["question"]
    response = llm.invoke(question)
    return {
        "answer":response.text,
        "messages":[question, response.text],
    }
def test():
    graph_builder = StateGraph(
        OverallState,
        input_schema=InputState,
        output_schema=OutputState,
    )
    
    graph_builder.add_node("chatbot", chatbot)
    graph_builder.add_edge(START, "chatbot")
    graph_builder.add_edge("chatbot", END) 
    
    graph = graph_builder.compile()

    # 터미널에서는 그래프를 보여줄 수 없음.    
    # try:
    #     display(Image(graph.get_graph().draw_mermaid_png()))
    # except Exception as e:
    #     print(f"Error displaying graph: {e}")
    png_data = graph.get_graph().draw_mermaid_png()
    Path("graph.png").write_bytes(png_data)

    
    result = graph.invoke({"question": "대한민국의 수도는 어디인가요?"})
    print(f"모델 응답: {result['answer']}")
    
###############################################################################
class State(TypedDict):
    messages: Annotated[list[str], add]
    question_length: int

def guradrail(state: State) -> State:
    question_length = len(state["messages"][-1])
    return {"question_length": question_length}

def chatbot2(state: State) -> State:
    question = state["messages"][-1]
    response = llm.invoke(question)
    return {
        "messages": [response.content]
    }

def routing_function(state: State) -> str:
    if state["question_length"] > 3:
        return "chatbot2"
    return END

def test2():
    graph_builder = StateGraph(State)
    graph_builder.add_node("guradrail", guradrail)
    graph_builder.add_node("chatbot2", chatbot2)
    
    graph_builder.add_conditional_edges(
        "guradrail",
        routing_function,
        {"chatbot2": "chatbot2", END: END}
    )
    graph_builder.add_edge(START, "guradrail")
    graph_builder.add_edge("chatbot2", END)
    graph = graph_builder.compile()
    
    png_data = graph.get_graph().draw_mermaid_png()
    Path("graph_2.png").write_bytes(png_data)
    
    print(graph.invoke({"messages": ["o"]}))
    
    print("--------------------------------------")
    
    print(graph.invoke({"messages": ["안녕하세요","안녕하세요! 어떻게 도와드릴까요?"], "question_length": 5}))