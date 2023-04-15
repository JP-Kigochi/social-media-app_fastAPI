from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated ="auto")

#Password hashing
def hash(password: str):
    return pwd_context.hash(password)

#verify password against hashed password
def verify(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)