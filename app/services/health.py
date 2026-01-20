
class HealthService:
    def __init__(self,users_client,posts_client):
        self.users_client = users_client
        self.posts_client = posts_client
    
    def check(self)->dict:
        return {
            "users_api":(
                "ok" if self.users_client.is_available() else "unavailable"
            ),
            "posts_api":(
                "ok" if self.posts_client.is_available() else "unavailable"
            ),
        }