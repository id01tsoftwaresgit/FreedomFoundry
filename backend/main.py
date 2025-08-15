from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from .core.config import settings
from .core.security import get_current_user
from .models.user import User as UserModel

# Create the FastAPI app instance
app = FastAPI(
    title="FreedomFoundry API",
    description="The backend API for the FreedomFoundry platform.",
    version="0.1.0"
)

# Configure CORS
# This allows the frontend (running on a different domain/port) to communicate with the backend.
if settings.FRONTEND_URL:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[settings.FRONTEND_URL],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

from .api import referrals

# --- API Routers ---
# Placeholder for future API routers
# from .api import auth, ventures, products
# app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])
# app.include_router(ventures.router, prefix="/api/v1/ventures", tags=["ventures"])
# app.include_router(products.router, prefix="/api/v1/products", tags=["products"])
app.include_router(referrals.router, prefix="/api/v1/referrals", tags=["Referrals"])


# --- Basic Endpoints ---

@app.get("/", tags=["Root"])
async def read_root():
    """
    Welcome endpoint for the API.
    """
    return {"message": "Welcome to the FreedomFoundry API!"}

@app.get("/api/health", tags=["Health Check"])
async def health_check():
    """
    Health check endpoint to verify that the API is running.
    """
    return {"status": "ok"}


# --- Protected Endpoints ---

@app.get("/api/v1/me", response_model=UserModel, tags=["Users"])
async def read_users_me(current_user: UserModel = Depends(get_current_user)):
    """
    Fetch the current authenticated user's profile.
    """
    return current_user

# To run the app locally:
# uvicorn backend.main:app --reload
