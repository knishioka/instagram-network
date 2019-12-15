from .base_model import BaseModel


class UserModel(BaseModel):
    """instagram user class for firestore."""

    collection = 'users'
    valid_keys = ['full_name', 'is_verified', 'biography',
                  'followees', 'followers', 'mediacount']
