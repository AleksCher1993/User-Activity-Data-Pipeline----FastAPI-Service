
class HealthService:
    def __init__(self,users_client,posts_client):
        self.users_client = users_client
        self.posts_client = posts_client
    
    def check(self)->dict:
        status={
            "users_api":"ok",
            "posts_api":"ok",
        }
        
        try:
            self.users_client.get_users()
        
        except Exception:
            status["users_api"]="unavailable"
            
        try:
            self.posts_client.get_posts()
        except Exception:
            status["posts_api"]="unavailable"
        
        return status