from pydantic import BaseModel,Field,field_validator,EmailStr

class UserActivity(BaseModel):
    user_id: int =Field(default=1, description="Уникальный идентификатор пользователя")
    name: str = Field(min_length=3, max_length=40,default="unknown",description="Полное имя",title="Имя пользователя")
    email: EmailStr
    city: str
    posts_count: int

    @field_validator("posts_count")
    @classmethod
    def check_posts(cls,value):
        if value < 0:
            raise ValueError("Колличество постов не должно быть меньше 0")
        return value
    
    @field_validator("user_id")
    @classmethod
    def check_id(cls,value):
        if value < 0:
            raise ValueError("Id не должен быть меньше 0")
        return value
    #валидатор для 
    @field_validator('name', mode='before')
    @classmethod
    def validate_name(cls, v):
        if isinstance(v, int):
            return str(v)
        elif isinstance(v, str):
            return v
        else:
            raise ValueError("Имя должно быть строкой или числом")
    
    
        