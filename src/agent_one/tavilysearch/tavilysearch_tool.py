from langchain.tools import tool
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch
@tool
def add (a: int, b: int) -> int:
    """Add two numbers together."""
    return a + b

@tool
def multiply(a: int, b: int) -> int:
    """Multiply two numbers together."""
    return a * b

def test():
    tools = [add, multiply]     
    llm = ChatOpenAI(model="gpt-4o")
    llm_with_tools = llm.bind_tools(tools)
    query = "3 곱하기 5는 뭔가요 ?  2 와 4를 더하면 뭔가요?"
    response = llm_with_tools.invoke(query)
    print(f"Response: {response}")
    print(f"response.tool_calls: \n{response.tool_calls}")
    
    print(f"{llm_with_tools.invoke('안녕하세요')}")
    print(f"response.tool_calls: \n{response.tool_calls}")
    
def tavilysearch_test():
    tool = TavilySearch(max_results=2)
    tools = [tool]

    llm = ChatOpenAI(model="gpt-4o")
    llm_with_tools = llm.bind_tools(tools)
    response = llm_with_tools.invoke('2026년 AI 트렌드는 무엇인가요?')
    print(f"{llm_with_tools.invoke('hello')}")
    print("-"*60)
    print(f"Response: {response}")
    print("-"*60)
    print(f"response.tool_calls: \n{response.tool_calls}")