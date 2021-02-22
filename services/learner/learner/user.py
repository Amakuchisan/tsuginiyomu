import domain.user
from db import user as db

def create(hatena_id: str):
# def createUser(hatena_id: str) -> domain.User:
    user = domain.user.User(hatena_id)
    print("hoge")
    print(user)
    print(user.hatena_id)
    return db.create(hatena_id)
