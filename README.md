# instagram-network
Network Analysis for Instagram

## Installation

```
pip install -r requirements.txt
```

## Getting Started
You need to set environment variables `INSTAGRAM_USER_ID` and `INSTAGRAM_PASSWORD` to get Instagram data.

### Examples

```
export INSTAGRAM_USER_ID=<your instagram id>
export INSTAGRAM_PASSWORD=<your instagram password>
python followee_list.py --users user_id1,user_id2,user_id3
```

## Store data in firebase
If you want to store data in firebase, you need to set `GOOGLE_APPLICATION_CREDENTIALS`.
