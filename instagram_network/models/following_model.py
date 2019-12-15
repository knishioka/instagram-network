from .base_model import BaseModel


class FollowingModel(BaseModel):
    """instagram user following list."""

    collection = 'followings'
    valid_keys = ['user_ids']
