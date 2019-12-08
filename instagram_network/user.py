import argparse
import instaloader
import json
from .loader import context


def get_profile(user_id, as_json=False):
    """Get user profile as json format

    Args:
        user_id (str): Instagram user_id.
        as_json (bool): json (True), dict (False)

    Returns:
        str: json formatted user profile

    Examples:
        >>> get_profile('target_username')
        '{"userid": 123456, "username": "target_username",...}'
    """
    profile = instaloader.Profile.from_username(context(), user_id)
    profile_dict = {
        'userid': profile.userid,
        'username': profile.username,
        'full_name': profile.full_name,
        'is_verified': profile.is_verified,
        'biography': profile.biography,
        'followees': profile.followees,
        'followers': profile.followers,
        'mediacount': profile.mediacount
    }
    if as_json:
        return json.dumps(profile_dict)
    else:
        return profile_dict


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Get a user profile')
    parser.add_argument('-u', '--user',
                        required=True,
                        help='instagram user ids')
    args = parser.parse_args()
    print(get_profile(args.user_id, as_json=True))
