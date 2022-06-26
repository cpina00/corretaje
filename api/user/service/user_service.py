from fastapi import HTTPException, status


from api.user.model.user_model import User as UserModel
from api.user.schema import user_schema
from api.user.service.auth_service import get_password_hash


def create_user(user: user_schema.UserRegister):

    get_user = UserModel.filter((UserModel.email == user.email) | (UserModel.username == user.username)).first()
    if get_user is not None:
        msg = "Email already registered"
        if get_user.username == user.username:
            msg = "Username already registered"
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=msg
        )

    db_user = UserModel(
        username=user.username,
        email=user.email,
        password=get_password_hash(user.password)
    )

    db_user.save()

    return user_schema.User(
        id = db_user.id,
        username = db_user.username,
        email = db_user.email
    )
    
def list_users():
    users = UserModel.filter()
    list_user = []
    for user in users:
        list_user.append(
            user_schema.User(
                id = user.id,
                email = user.email,
                username = user.username,              
            )
        )
    return list_user