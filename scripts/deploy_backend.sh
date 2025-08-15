#!/bin/bash

# === Backend Deployment Guide ===
#
# We recommend deploying the backend using Render for its excellent free tier
# for web services and Python support.
#
# --- Recommended Method: Render Git Integration ---
#
# 1. Push your repository to GitHub, GitLab, or Bitbucket.
# 2. Go to your Render dashboard (https://dashboard.render.com).
# 3. Click "New" -> "Web Service".
# 4. Connect your Git repository.
# 5. Render will ask you to configure the service. Use the following settings:
#    - Name: freedomfoundry-backend (or your choice)
#    - Root Directory: `backend`
#    - Environment: Python 3
#    - Region: Your choice
#    - Branch: main (or your deployment branch)
#    - Build Command: `pip install -r requirements.txt`
#    - Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
#
# 6. Choose the "Free" instance type.
#
# 7. **IMPORTANT:** Under "Advanced", you must add your environment variables.
#    - Go to the "Environment" tab.
#    - Add the following secrets, using the values from your local `.env` file:
#      - `SUPABASE_URL`
#      - `SUPABASE_KEY` (the public anon key)
#      - `SUPABASE_SERVICE_ROLE_KEY` (the secret service key)
#      - `FRONTEND_URL` (the URL of your deployed Vercel frontend)
#
# 8. Click "Create Web Service". Render will build and deploy your API.
#    The first build may take a few minutes.
#
# --- Post-Deployment ---
#
# - Your API will be available at the URL provided by Render (e.g., `https://freedomfoundry-backend.onrender.com`).
# - Note that free-tier services on Render may "spin down" after a period of
#   inactivity and take 30-60 seconds to start up on the first request.
#
# --- Alternative Method: Render CLI ---
#
# While possible, Render's primary workflow is Git-based. For CLI deployments,
# you would typically use Docker. The Git-based approach is recommended for this project.
#
echo "This script is a guide. Please follow the instructions above to deploy the backend."
echo "The recommended method is using Render's Git integration."
exit 0
