from app.exceptions.custom import DataProcessingError


def build_posts_count(posts: list[dict]) -> dict[int, int]:
    if not posts:
        raise DataProcessingError("Posts data is empty")

    count: dict[int, int] = {}
    for post in posts:
        user_id = post["userId"]
        count[user_id] = count.get(user_id, 0) + 1

    return count


def build_users_activity(
    users: list[dict],
    posts: list[dict],
) -> list[dict]:

    if not users or not posts:
        raise DataProcessingError("Users or posts data is empty")

    posts_count = build_posts_count(posts)

    activity: list[dict] = []
    for user in users:
        activity.append({
            "user_id": user["id"],
            "name": user["name"],
            "email": user["email"],
            "city": user["address"]["city"],
            "posts_count": posts_count.get(user["id"], 0),
        })

    return activity


def get_top_users(
    users_activity: list[dict],
    limit: int,
) -> list[dict]:

    if not users_activity:
        raise DataProcessingError("Users activity is empty")

    return sorted(
        users_activity,
        key=lambda x: x["posts_count"],
        reverse=True
    )[:limit]