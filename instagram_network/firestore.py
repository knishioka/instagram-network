import firebase_admin
import instaloader
from datetime import datetime
from firebase_admin import firestore
from .loader import context


def connection():
    """Create connection to firebase."""
    if (not len(firebase_admin._apps)):
        firebase_admin.initialize_app()
    return firestore.client()


def store_user(profile, attrs={}):
    """Store user profile in firebase.

    Args:
        profile (instaloader.structures.Profile): user profile instance.
        attrs (dict): additional user attributes.

    Returns:
        google.cloud.firestore_v1.types.WriteResult

    Examples:
        >>> profile = instaloader.Profile.from_username(context(), 'shinzoabe')
        >>> store_user(profile)
        update_time {
            seconds: 1575904566
            nanos: 49912000
        }

    """
    db = connection()
    doc_ref = db.document(f'users/{profile.username}')
    profile_dict = {
        'userid': profile.userid,
        'full_name': profile.full_name,
        'is_verified': profile.is_verified,
        'biography': profile.biography,
        'followees': profile.followees,
        'followers': profile.followers,
        'mediacount': profile.mediacount,
        'stored_at': datetime.now()
    }

    valid_attr_keys = ['is_artist', 'is_gallery',
                       'price_max', 'price_min', 'price_avg']
    valid_attrs = {k: attrs.get(k) for k in valid_attr_keys}

    return doc_ref.set({**profile_dict, **valid_attrs})


def fetch_user(userid, store_if_not_exists=True):
    """Fetch user data from firebase.

    Args:
        userid (str): instagram user id.
        store_if_not_exists (boolean): get data from instagram if not exists.

    Returns:
        dict: user profile dict.

    Examples:
        >>> fetch_user("shinzoabe")
        {'full_name': '安倍晋三',
         'followees': 22,
         'followers': 488862,
         'is_verified': True,
         'mediacount': 409,
         'userid': 6738899121,
         'biography': ''}

    """
    db = connection()
    res = db.document(f"users/{userid}").get().to_dict()
    if res is None and store_if_not_exists:
        return update_user(userid)
    else:
        return res


def update_user(userid, attrs={}):
    """Update user data.

    Args:
        userid (str): instagram user id.
        attrs (dict): additional user attributes.

    Returns:
        dict: user profile dict.

    Examples:
        >>> update_user("shinzoabe")
        {'full_name': '安倍晋三',
         'followees': 22,
         'followers': 488862,
         'is_verified': True,
         'mediacount': 409,
         'userid': 6738899121,
         'biography': ''}

    """
    profile = instaloader.Profile.from_username(context(), userid)
    store_user(profile, attrs)
    return fetch_user(userid, store_if_not_exists=False)
