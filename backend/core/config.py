from pydantic_settings import BaseSettings, SettingsConfigDict
import os

# Load .env file from the correct path if it exists
# This is useful for local development.
# The backend directory is the root for this context.
dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')

class Settings(BaseSettings):
    """
    Application settings are defined here.
    These settings are loaded from environment variables.
    For local development, a .env file can be used.
    """
    APP_ENV: str = "development"
    FRONTEND_URL: str = "http://127.0.0.1:5500"

    SUPABASE_URL: str
    SUPABASE_KEY: str # This is the anon key
    SUPABASE_SERVICE_ROLE_KEY: str

    model_config = SettingsConfigDict(env_file=dotenv_path, extra='ignore')

# Create a single instance of the settings to be used throughout the application
settings = Settings()
