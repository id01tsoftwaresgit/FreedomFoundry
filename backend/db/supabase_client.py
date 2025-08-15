from supabase import create_client, Client
from ..core.config import settings

# It's good practice to have two clients:
# 1. anon_client: Uses the public anonymous key, suitable for operations that should be allowed for any user.
# 2. service_client: Uses the secret service role key, for admin-level operations on the backend.

anon_client: Client | None = None
service_client: Client | None = None

try:
    # This client is for public-facing operations, respecting RLS policies
    anon_client = create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)

    # This client is for backend operations, bypassing RLS. Use with caution.
    service_client = create_client(settings.SUPABASE_URL, settings.SUPABASE_SERVICE_ROLE_KEY)

except Exception as e:
    print(f"Error initializing Supabase clients: {e}")
    print("Please ensure SUPABASE_URL, SUPABASE_KEY, and SUPABASE_SERVICE_ROLE_KEY are set in your environment or .env file.")
