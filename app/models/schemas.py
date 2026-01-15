from pydantic import BaseModel

class UserActivity(BaseModel):
    user_id: int
    name: str
    email: str
    city: str
    posts_count: int
