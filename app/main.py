from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import post, user, auth, vote

#Creating the FastAPI application
app = FastAPI()

#Allow all URLs to make requests to our API
origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#Including routes into our FastAPI application
app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

#Creating the default route
@app.get("/")
def root():
    return {"message": "Hello World!"}