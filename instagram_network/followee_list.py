import argparse
import instaloader
import json
import sys
from instagram_network.loader import context


def main(*, user_ids):
    all_followees = [{user_id: followees(user_id)} for user_id in user_ids]
    print(json.dumps({'followees': all_followees}))


def followees(user_id):
    """Get followees.

    Args:
        user_id (str): Instagram user_id.

    Returns:
        list of str: followee id list.

    Examples:
        >>> followees(target_user_id)
        ['followee1', 'followee2', 'followee3']
    """
    print(f"Getting {user_id}'s followees.", file=sys.stderr)
    profile = instaloader.Profile.from_username(context(), user_id)
    followee_list = [followee.username for followee in profile.get_followees()]
    output = f'{user_id}_followees.json'
    with open(output, 'w') as io:
        print(f"Writing {user_id}'s followees to {output}.", file=sys.stderr)
        json.dump({user_id: followee_list}, io)
    return followee_list


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Get followees list')
    parser.add_argument('-u', '--users',
                        required=True,
                        help='commma separated instagram user ids')
    args = parser.parse_args()
    user_ids = args.users.split(',')
    main(user_ids=user_ids)
