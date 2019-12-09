import firebase_admin
from firebase_admin import firestore


def initialize():
    if (not len(firebase_admin._apps)):
        return firebase_admin.initialize_app()


def store_user(profile):
    """Store user profile in firebase.

    Args:
        profile (instaloader.structures.Profile): user profile instance.

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
    initialize()
    db = firestore.client()
    doc_ref = db.document(f'users/{profile.username}')

    return doc_ref.set({
        'userid': profile.userid,
        'full_name': profile.full_name,
        'is_verified': profile.is_verified,
        'biography': profile.biography,
        'followees': profile.followees,
        'followers': profile.followers,
        'mediacount': profile.mediacount
    })
