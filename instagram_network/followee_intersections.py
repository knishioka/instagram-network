import glob
import json
import pandas as pd
from functools import reduce


def main():
    files = glob.glob('*_*.json')
    targets = [json.load(open(file)) for file in files]
    all_followee_list = reduce(lambda x, y: {**x, **y}, targets, dict())
    df = pd.DataFrame({k: list_to_true_value_dict(v)
                       for k, v in all_followee_list.items()}).fillna(False)
    df.sum(axis=1).sort_values(ascending=False).to_csv('intersections.csv')


def list_to_true_value_dict(user_list):
    """Convert list to dict with True for Pandas Dataframe.

    Args:
        user_list (list of str): user_id list.

    Returns:
        dict: list is converted to dict keys and all dict values are True.

    Examples:
        >>> list_to_relation_dict(['a', 'b', 'c'])
        {'a': True, 'b': True, 'c': True}

    """
    return {user: True for user in user_list}


if __name__ == '__main__':
    main()
