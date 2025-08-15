from fastapi import APIRouter, Depends, HTTPException
from ..core.security import get_current_user
from ..db.supabase_client import service_client
from gotrue.types import User

router = APIRouter()

@router.get("/stats", tags=["Referrals"])
async def get_referral_stats(
    current_user: User = Depends(get_current_user)
):
    """
    Get statistics for the current user's referrals.
    For now, it just gets the total number of signups.
    """
    supabase = service_client
    if not supabase:
        raise HTTPException(status_code=503, detail="Supabase client not available")

    try:
        # This assumes a 'referrals' table exists with a 'referrer_id' column.
        # The frontend will need to be updated to call this endpoint.
        response = supabase.table('referrals').select('id', count='exact').eq('referrer_id', str(current_user.id)).execute()

        signup_count = response.count if response.count is not None else 0

        return {
            "signups": signup_count,
            "commission": "$0.00" # Placeholder for commission tracking
        }
    except Exception as e:
        # This might happen if the table doesn't exist yet.
        # For now, we return a default value in case of error.
        print(f"Could not fetch referral stats: {e}")
        return {
            "signups": 0,
            "commission": "$0.00",
            "error": "Could not fetch stats. Ensure the 'referrals' table is set up correctly."
        }
