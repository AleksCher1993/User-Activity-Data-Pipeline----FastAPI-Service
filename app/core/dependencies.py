from fastapi import Depends
from app.core.config import settings
from app.services.fetcher import fetch_user_data, fetch_posts_data
from app.services.clients import UsersClient, PostsClient
from app.services.health import HealthService
from app.services.service import UserActivityService


def get_users_client():
    users = fetch_user_data(settings.URL_USER)
    return UsersClient(users)


def get_posts_client():
    posts = fetch_posts_data(settings.URL_POSTS)
    return PostsClient(posts)

def get_health_service(
    users_client=Depends(get_users_client),
    posts_client=Depends(get_posts_client),
):
    return HealthService(users_client, posts_client)

def get_user_activity_service(
    users_client=Depends(get_users_client),
    posts_client=Depends(get_posts_client),
):
    return UserActivityService(users_client, posts_client)

