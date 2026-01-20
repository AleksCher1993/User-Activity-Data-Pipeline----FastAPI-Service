class UsersClient:
    def __init__(self,users_data):
        self.users_data=users_data

    def get_users(self):
        return self.users_data
    

class PostsClient:
    def __init__(self,posts_data):
        self.posts_data=posts_data

    def get_posts(self):
        return self.posts_data
   