# instagram-network
Network Analysis for Instagram

## Installation

```bash
pip install -r requirements.txt
```

## Getting Started
You need to set environment variables `INSTAGRAM_USER_ID` and `INSTAGRAM_PASSWORD` to get Instagram data.

### Examples

```bash
export INSTAGRAM_USER_ID=<your instagram id>
export INSTAGRAM_PASSWORD=<your instagram password>
python followee_list.py --users user_id1,user_id2,user_id3
```

## Store data in firebase
If you want to store data in firebase, you need to set `GOOGLE_APPLICATION_CREDENTIALS`.

### Store User Data

```python
from instagram_network.models import UserModel

UserModel.create(doc_id='user_id', attrs={'full_name': 'User Name', 'is_verified': False})
```

### Store Following Relationship

```python
from instagram_network.models import FollowingModel

FollowingModel.create(doc_id='follower_id',
                      attrs={'user_ids': ['followee1', 'followee2', followee3]})
```
