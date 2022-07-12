from asyncio.selector_events import BaseSelectorEventLoop
from operator import truediv
from fastapi import HTTPException, status
from psycopg2 import IntegrityError


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
    list_user = []
    for user in UserModel.select().order_by(UserModel.id):
        list_user.append(
            user_schema.User(
                id = user.id,
                email = user.email,
                username = user.username,              
            )
        )
    return list_user

def get_user(id:int):
    try:
        get_user = UserModel.get(UserModel.id==id)
        user = user_schema.User(
        id = get_user.id,
        email = get_user.email,
        username = get_user.username
        )
        return user   
    except:
        msg = "Id user not found"
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=msg
        )

def delete_user(id:int):
    try:
        user = UserModel.get(UserModel.id==id)
        user.delete_instance()
    except:
        msg = "Id user not found"
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=msg
        )
        
def edit_user(user_update: user_schema.User):
    email = exist_email_user(user_update)
    print("En edit user")
    if email:
        print("El correo ya existe, intente con otro")
        msg = "Error, email is exist in other user"
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=msg
        )
    else:
        try:        
            user = UserModel.get(UserModel.id == user_update.id)
            user.username = user_update.username
            user.email = user_update.email
            print("tengo actualizado los valores")
            print("Voy a guardar en la db")
            user.save()
            print("Usuario guardado en la db")
            user_edit = user_schema.User(
                email = user.email,
                username = user.username,
                id = user.id
            )
            return user_edit
        except BaseException as err:
                msg = "ID User Not Found"
                raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                    detail=msg
            )

def exist_email_user(user):
    try:
        query = UserModel.select().where(UserModel.email == user.email).get()
        print(f"query.id: {query.id}, user.id: {user.id}")
        if query.id != user.id:
            return True
    except:
        return False