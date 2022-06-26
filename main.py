from fastapi import FastAPI


from api.user.route.user_route import route as user_route
app = FastAPI()

app.include_router(user_route)

@app.get("/")
def home():
    return {"hello":"world"}