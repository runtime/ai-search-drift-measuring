from fastapi import FastAPI
from app.api import endpoints  # Import your API endpoints

print("Main module loaded!")

# Initialize FastAPI app
app = FastAPI()

# Include API routers
app.include_router(endpoints.router)

# Define a basic root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the AI Search Drift Measuring API!"}
