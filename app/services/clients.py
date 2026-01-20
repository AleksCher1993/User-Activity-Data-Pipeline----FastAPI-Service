class UsersClient:
    def __init__(self,users_data=None,error:Exception | None=None):
        self.users_data=users_data
        self.error=error

    def is_available(self) -> bool:
        return self.error is None
    def get_users(self):
        if self.error:
            raise self.error
        return self.users_data
    

class PostsClient:
    def __init__(self,posts_data=None,error:Exception | None=None):
        self.posts_data=posts_data
        self.error=None
    def is_available(self) -> bool:
        return self.error is None
    def get_posts(self):
        if self.error:
            raise self.error
        return self.posts_data
   