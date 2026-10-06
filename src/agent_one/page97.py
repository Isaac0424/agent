from pydantic import BaseModel, Field

class User(BaseModel):
    id: int = Field(..., description="The unique identifier for the user")
    name: str = Field(..., description="The name of the user")
    email: str = Field(..., description="The email address of the user" )

def test() -> str:
    user_data={
        "id": 1,
        "name": "Alice",
        "email": "alice@example.com"
    }

    user1 = User(**user_data)
    print(user1)