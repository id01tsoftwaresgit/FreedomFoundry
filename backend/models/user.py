from pydantic import BaseModel, EmailStr
from typing import Optional, Dict, Any
from datetime import datetime
import uuid

class User(BaseModel):
    """
    Pydantic model for a user, based on Supabase's user object.
    """
    id: uuid.UUID
    email: Optional[EmailStr] = None
    last_sign_in_at: Optional[datetime] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
