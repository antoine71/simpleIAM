import bcrypt


def hash_password(password: str):
    pass_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return pass_hash.decode()


def validate_password(password: str, pass_hash: str):
    return bcrypt.checkpw(password.encode(), pass_hash.encode())
