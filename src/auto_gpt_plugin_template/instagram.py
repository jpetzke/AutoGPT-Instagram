import instabot
from . import AutoGPT_Instagram

plugin = AutoGPT_Instagram()

bot = instabot.Bot()
bot.login(username=plugin.instagram_username, password=plugin.instagram_password)


def post_instagram_photo(photo_path: str, caption: str) -> str:
    """
    Post a photo to Instagram.

    Args:
        photo_path (str): The path to the photo.
        caption (str): The caption for the photo.
    
    Returns:
        str: The URL of the photo.
    """

    bot.upload_photo(photo_path, caption=caption)
    return f"Posted photo to Instagram: {bot.last_media_id}"


