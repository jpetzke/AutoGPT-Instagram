import instabot
from . import AutoGPT_Instagram
import os
import requests

bot = instabot.Bot()

def login_instagram(username, password) -> bool:
    """Login to Instagram.

    Returns:
        bool: True if the login was successful.
    """

    return bot.login(username=username, password=password)


def post_instagram_photo(photo_path: str, caption: str) -> str:
    """
    Post a photo to Instagram.

    Args:
        photo_path (str): The path to the photo.
        caption (str): The caption for the photo.
    
    Returns:
        str: The URL of the photo.
    """

    path = os.path.join("auto_gpt_workspace", photo_path)

    response = bot.upload_photo(path, caption=caption)

    os.rename(path, path.removesuffix(".REMOVE_ME"))

    if not response:
        return "Failed to post photo to Instagram."

    print(response)
    return f"Posted photo to Instagram. Url=https://www.instagram.com/p/{response['media']['code']}"



def search_instagram_users(query: str):
    url = f"https://www.instagram.com/web/search/topsearch/?query={query}"
    response = requests.get(url)
    response_json = response.json()
    users = response_json['users']
    result = []
    for user in users:
        user_info = {
            'username': user['user']['username'],
            'full_name': user['user']['full_name'],
            'is_private': user['user']['is_private'],
            'is_verified': user['user']['is_verified'],
        }
        result.append(user_info)
    
    # Sort the list alphabetically by username
    result = sorted(result, key=lambda x: (x['username']))

    # Put verified users first
    result = sorted(result, key=lambda x: (x['is_verified']), reverse=True)


    return result[:20]


def follow_instagram_user(username: str):
    if bot.follow(username):
        return f"Followed {username}"
    else:
        return f"Failed to follow {username}"
    
    
def unfollow_instagram_user(username: str):
    if bot.unfollow(username):
        return f"Unfollowed {username}"
    else:
        return f"Failed to unfollow {username}"