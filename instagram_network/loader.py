import instaloader
import os
from functools import lru_cache


@lru_cache(maxsize=None)
def context():
    """Get logged in context.

    Returns:
        InstaloaderContext: logged in context.

    Examples:
        >>> loader_context()
        <instaloader.instaloadercontext.InstaloaderContext at 0x111456e10>

    """
    loader = instaloader.Instaloader()
    loader.login(os.environ['INSTAGRAM_USER_ID'],
                 os.environ['INSTAGRAM_PASSWORD'])
    return loader.context
