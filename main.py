from fastapi import FastAPI

from api.utils.create_tables import create_tables

from api.user.route.user_route import route as user_route
app = FastAPI()

app.include_router(user_route)

@app.get("/")
def home():
    return {"hello":"world"}

if __name__=="__main__":
    create_tables()