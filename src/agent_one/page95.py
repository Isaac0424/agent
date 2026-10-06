from typing import TypedDict
    
class User(TypedDict):
    id: int
    name: str
    email: str


    
def get_info(user: User) -> str:
    return f"User ID: {user['id']}, Name: {user['name']}, Email: {user['email']}"


def test_typedic():
    user: User = User(id=1, name="Alice", email="alice@example.com")
    print(f"데이터 타입에 맞는 입력에 대한 출력 : \n{get_info(user)}")
    
def wrong_typedic():
    user: User = User(id=1, name=123, email="alice@example.com")
    print(f"데이터 타입과 다른 입력이지만 문제가 발생하지 않는 TypedDict: \n{get_info(user)}")
    
def test():
    test_typedic()
    wrong_typedic()