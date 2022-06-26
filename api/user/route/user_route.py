from fastapi import APIRouter
from fastapi import status

from fastapi import Depends
from fastapi import Body
from fastapi import Header

from fastapi.security import OAuth2PasswordRequestForm

from typing import Union
from typing import List


from api.user.schema import user_schema
from api.user.service import user_service
from api.user.service import auth_service
from api.user.schema.token_schema import Token

from api.utils.db import get_db
from api.user.service.auth_service import get_current_user 
from api.user.service.user_service import list_users

from typing import Union

from api.user.model.user_model import User as UserModel


route = APIRouter(
    prefix="/api",
    tags=["users"]
)


@route.post(
    "/login",
    response_model=Token
)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    ## Login for access token
    
    ## Args
    The app can receive next fields by form data
    - username: Your username or email
    - password: Your password
    
    ## Return
    - access token and token type
    """
    
    access_token = auth_service.generate_token(form_data.username, form_data.password)
    return Token(access_token=access_token, token_type="bearer")




@route.get(
    "/",
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(get_db)],
    response_model=List[user_schema.User],
    )
def home():
    """return a list with all users en the system"""
    return list_users()

@route.get(
    "/{id}",
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(get_db), Depends(get_current_user)],
    summary="Summari donde estás?"
    )
def detail_user(id:int):
    """return the detail a user id"""
    return {"The user is":id}


@route.post(
    "/user/", 
    status_code=status.HTTP_201_CREATED,
    response_model=user_schema.User,
    dependencies = [Depends(get_db)],
    summary = "Create a new user"    
)
def create_user(user: user_schema.UserRegister = Body(...)):
    """
    Create a new user in the app
    
    ### args
    the app can receive next fields into a JSON
    - email: A valid email
    - username: Unique username
    - password: Strong password for authentication
    
    ### returns
    - user: User info
    """
    return user_service.create_user(user)



@route.delete(
    "/{id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_user(id:int):
    message = f"resouce {id} delete successful"
    return message

@route.put(
    "/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def update_user(id:int):
    message = f"resouce {id} update successful"
    return message


@route.get("/header/", tags=["header"])
async def read_items(user_agent: Union[str, None] = Header(default=None), data = None):
    if user_agent=="hola":
        return {"esto": "Funcionó!!!", "data":data}
    return {"User-Agent": user_agent}

