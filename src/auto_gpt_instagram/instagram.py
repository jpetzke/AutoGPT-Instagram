import instabot
from . import AutoGPT_Instagram
import os

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


