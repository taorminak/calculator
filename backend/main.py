from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import auth, calculator, users

# Create a FastAPI instance
app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://127.0.0.1:5173",
    "http://localhost:5173",
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    "http://127.0.0.1:51186",
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Authorization", "Content-Type"],
)

# Include the authentication, calculator, and user routers
app.include_router(auth.router)
app.include_router(calculator.router)
app.include_router(users.router)


# Define the root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the Calculator API"}
