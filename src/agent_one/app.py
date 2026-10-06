from .page86 import page86_ai_msg
from . import page95
from . import page97
from . import page99_reducer
from . import page101_graph
from . import page105_agent
from .tavilysearch import exam1
from .tavilysearch.tavilysearch_tool import add, multiply
from .tavilysearch.tavilysearch_tool import tavilysearch_test
def sub_hello() -> None:
    print("Hello, World!")
    print(f"{__name__} is running as the main module.")
    

def main() -> None:
    sub_hello()
    # page86_ai_msg()
    # page95.test()
    # page97.test()
    # page99_reducer.test()
    # page101_graph.test()
    # page105_agent.test2()
    tavilysearch_test()