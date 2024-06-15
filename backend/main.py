from fastapi import FastAPI
from routers import auth, calculator, users

# Create a FastAPI instance
app = FastAPI()

# Include the authentication, calculator, and user routers
app.include_router(auth.router)
app.include_router(calculator.router)
app.include_router(users.router)

# Define the root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the Calculator API"}
