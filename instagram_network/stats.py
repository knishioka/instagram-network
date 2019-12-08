import instaloader
from .loader import context


def follower_followee_count(user_id):
    """Get follower and followee count.

    Args:
        user_id (str): instagram user_id.

    Returns:
        dict: follower count and followee count.

    Examples:
        >>>follower_followee_count('shinzoabe')
        {'follower_cnt': 487315, 'followee_cnt': 22}

    """
    profile = instaloader.Profile.from_username(context(), user_id)
    return {'follower_cnt': profile.followers,
            'followee_cnt': profile.followees}
