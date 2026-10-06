from typing import TypedDict, Annotated
from operator import add
from langgraph.graph import StateGraph
from langgraph.graph import START, END


class State(TypedDict):
    messages: Annotated[list[str], add]
    
    
def chatbot(state: State):
    question = state["messages"]
    answer = f"사용자 입력을 그대로 반환하는 챗봇입니다. \n{question} 라는 질문을 받았습니다."
    return {"messages": [answer]}

def routing_function(state: State):
    if len(state["messages"])> 1000:
        return True
    return False


def test():
    graph = StateGraph(State)
    graph.add_node("chatbot", chatbot)
    graph.add_node("routing", routing_function)
    graph.add_edge(START, "chatbot")
    graph.add_edge("chatbot", END)
    
    # graph.add_edge("node_a", "node_b")
    
    graph.add_conditional_edges(
        "chatbot",
        routing_function,
        {True: END, False: END}
        # {True: "summary",False: END}
    )
    
    app = graph.compile()
    
    result = app.invoke({
        "messages": ["Hello, how are you?"],
    })
    print(result)