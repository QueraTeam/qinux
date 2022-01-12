import os
import pwd
from uuid import uuid4


def run_as_user(user_id):
    def wrapper(func):
        def wrapped(*args, **kwargs):
            pid = os.fork()
            if pid == 0:
                os.setuid(user_id)
                func(*args, **kwargs)
                os._exit(0)
        return wrapped
    return wrapper


def make_root_only(path):
    os.system(f'chmod -R go-rwx {path}')


def create_user(username=None):
    if username is None:
        username = uuid4().hex
    os.system(f'adduser --disabled-password --gecos "" --no-create-home {username} >/dev/null')
    user_id = pwd.getpwnam(username).pw_uid
    return user_id
