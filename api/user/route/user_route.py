from fastapi import APIRouter
from fastapi import status

route = APIRouter(prefix="/user")


@route.get(
    "/",
    tags=["user"],
    status_code=status.HTTP_200_OK,
    )
def home():
    """return a list with all the user en the system"""
    return {"User":"list"}

@route.get(
    "/{id}",
    tags=["user"],
    status_code=status.HTTP_200_OK,
    )
def home(id:int):
    """return the detail a user id"""
    return {"The user is":id}


@route.post(
    "/",
    tags=["user"],
    status_code=status.HTTP_201_CREATED
)
def create_user():
    """Create user in this endpoind.
    The format is:
    -
    -
    -
    """
    return "Create user"

@route.delete(
    "/{id}",
    tags=["user"],
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_user(id:int):
    message = f"resouce {id} delete successful"
    return message

@route.put(
    "/{id}",
    tags=["user"],
    status_code=status.HTTP_204_NO_CONTENT,
)
def update_user(id:int):
    message = f"resouce {id} update successful"
    return message