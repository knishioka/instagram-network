import argparse


def main(*, user_ids):
    print(user_ids)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Get followees list')
    parser.add_argument('-u', '--users',
                        required=True,
                        help='commma separated instagram user ids')
    args = parser.parse_args()
    user_ids = args.users.split(',')
    main(user_ids=user_ids)
