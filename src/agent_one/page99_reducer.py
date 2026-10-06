from typing import TypedDict, Annotated
from langchain_core.messages import AIMessage, HumanMessage
from langgraph.graph.message import AnyMessage, add_messages

def add(left,right):
    return left + right

class User(TypedDict):
    messages: Annotated[list[str], add]

class State(TypedDict):
    messages: Annotated[list[AnyMessage], add_messages]
    
msg1 = [HumanMessage(content="Hello, how are you?", id="1")]
msg2 = [AIMessage(content="I'm doing well, thank you!", id="2")]
def test():
    added_messages = add_messages(msg1, msg2)
    
    print(f"Added Messages: {added_messages}")

