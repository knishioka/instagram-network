from .base_model import BaseModel


class UserModel(BaseModel):
    collection = 'users'
    valid_keys = ['full_name', 'is_verified', 'biography',
                  'followees', 'followers', 'mediacount']
