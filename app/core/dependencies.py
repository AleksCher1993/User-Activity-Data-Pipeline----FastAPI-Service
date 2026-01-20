from app.services.processor import get_posts, get_top_activity, get_users, get_users_activity
class UserActivityService:
    def get_users(self):
        return get_users()
    def get_posts(self):
        return get_posts()
    def get_users_activity(self):
        users=get_users()
        posts=get_posts()
        return get_users_activity(users,posts)
    def get_top_activity(self,limit:int):
        activity=self.get_users_activity()
        return get_top_activity(activity,limit)
def get_user_activity_service():    
    return UserActivityService()