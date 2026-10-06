from langchain_tavily import TavilySearch


def test():
    tool = TavilySearch(max_results=3)
    query = "What is the capital of South Korea?"
    result = tool.invoke(query)
    print(f"Search results for '{query}':")
    for idx, item in enumerate(result["results"], start=1):
        print(f"{idx}. {item['title']} - {item['url']}")
