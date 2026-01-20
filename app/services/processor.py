import os
from dotenv import load_dotenv
import logging

from app.services.fetcher import fetch_posts_data, fetch_user_data
logger = logging.getLogger(__name__)


load_dotenv()
def get_users():
    url_user=os.environ.get("URL_USER")
    users=fetch_user_data(url_user)
    return users
def get_posts():
    url_posts=os.environ.get("URL_POSTS")
    posts=fetch_posts_data(url_posts)
    return posts
def get_users_activity(users,posts):
    if not posts or not users:
        logger.warning("No data provided to get users activity.")
        return []
    count_dict=create_posts_count_dict(posts)
    user_act=create_user_activity(users,count_dict)
    return user_act
def get_top_activity(users_activity,limit):
    if users_activity is None or limit is None:
        logger.warning("No data provided to get top users activity.")
        return []
    user_act=sorted(users_activity,key=lambda x: x["posts_count"] if x else 0,reverse=True)[:limit]
    
    return user_act
#================================================
#================================================
#================================================
#handlers for def get_users_activity(users,posts)
def create_user_activity(users, posts_count_dict):
    if users is None or posts_count_dict is None:
        logger.warning("No data provided to create user activity.")
    user_activity=[]
    for user in users:
        user_activity.append(create_data_dict(user,posts_count_dict[user["id"]]))
    logger.info("Successfully created user activity and validate was good!")

    return user_activity
def create_data_dict(user,count):
    data_dict={
        "user_id":user["id"],
        "name":user["name"],
        "email":user["email"],
        "city":user["address"]["city"],
        "posts_count":count
    }
    return data_dict
def create_posts_count_dict(posts):
    if not posts:
        logger.warning("No posts data provided to get posts count dictionary!")
        return {}
    count_dict={}
    for post in posts:
        count_dict[post["userId"]] = count_dict.get(post["userId"], 0) + 1
    logger.info("Successfully created posts count dictionary")
    return count_dict
