from app.services.processor import (
    build_users_activity,
    get_top_users,
)

class UserActivityService:
    def __init__(self, users_client, posts_client):
        self.users_client = users_client
        self.posts_client = posts_client

    def get_users(self):
        return self.users_client.get_users()

    def get_posts(self):
        return self.posts_client.get_posts()

    def get_users_activity(self):
        users = self.get_users()
        posts = self.get_posts()
        return build_users_activity(users, posts)

    def get_top_activity(self, limit: int):
        activity = self.get_users_activity()
        return get_top_users(activity, limit)
