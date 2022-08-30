try:
    from .local_settings import *
except ImportError:
    from .production import *
