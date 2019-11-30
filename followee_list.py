import argparse
import instaloader
import os
from functools import lru_cache


def main(*, user_ids):
    print(user_ids)


@lru_cache(maxsize=None)
def loader_context():
    """Get logged in context.

    Returns:
        InstaloaderContext: logged in context.

    Examples:
        >>> loader_context()
        <instaloader.instaloadercontext.InstaloaderContext at 0x111456e10>
    """

    loader = instaloader.Instaloader()
    loader.login(os.environ['INSTAGRAM_USER_ID'],
                 os.environ['INSTAGRAM_PASSWORD'])
    return loader.context


def followees(user_id):
    profile = instaloader.Profile.from_username(loader_context(), user_id)
    return [followee.username for followee in profile.get_followees()]


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Get followees list')
    parser.add_argument('-u', '--users',
                        required=True,
                        help='commma separated instagram user ids')
    args = parser.parse_args()
    user_ids = args.users.split(',')
    main(user_ids=user_ids)
