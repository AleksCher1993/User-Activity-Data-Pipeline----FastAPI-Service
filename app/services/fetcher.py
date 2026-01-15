import requests
import logging



def fetch_user_data(URL_user:str):
    logging.info(f"Fetching user data from {URL_user}")
    try:
        with requests.Session() as session:
            response = session.get(URL_user, timeout=10)
            response.raise_for_status()
            users_data = response.json()
            logging.info(f"Successfully fetched user data from {URL_user}")
            return users_data
    except requests.RequestException as e:
        logging.error(f"Error fetching user data: {e}")
        return None

def fetch_posts_data(URL_posts:str):
    logging.info(f"Fetching posts data from {URL_posts}")
    try:
        with requests.Session() as session:
            response = session.get(URL_posts, timeout=10)
            response.raise_for_status()
            posts_data = response.json()
            logging.info(f"Successfully fetched posts data from {URL_posts}")
            return posts_data
    except requests.RequestException as e:
        logging.error(f"Error fetching posts data: {e}")
        return None
