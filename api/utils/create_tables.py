from api.user.model.user_model import User

from api.utils.db import db

def create_tables():
    with db:
        db.create_tables([User])