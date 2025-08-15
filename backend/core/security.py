from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from supabase import Client
from ..db.supabase_client import service_client
from gotrue.types import User

# Define the security scheme
reusable_bearer = HTTPBearer()

def get_current_user(
    token: HTTPAuthorizationCredentials = Depends(reusable_bearer),
    supabase: Client = Depends(lambda: service_client)
) -> User:
    """
    FastAPI dependency to get the current user from a Supabase JWT.

    This function validates the bearer token and returns the user object
    if the token is valid. Otherwise, it raises an HTTPException.
    """
    if not supabase:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Supabase client is not available."
        )

    try:
        # The token is extracted from "Bearer <token>"
        jwt = token.credentials
        user_response = supabase.auth.get_user(jwt)

        if user_response and user_response.user:
            return user_response.user

        # This part should ideally not be reached if get_user works as expected
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
        )

    except Exception as e:
        # Supabase client might raise an exception for invalid tokens
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Invalid authentication credentials: {e}",
            headers={"WWW-Authenticate": "Bearer"},
        )

# Dependency to get the user, can be used in path operations
# Example: @app.get("/users/me", response_model=User)
# async def read_users_me(current_user: User = Depends(get_current_user)):
#     return current_user
