#!/bin/bash

# === Frontend Deployment Guide ===
#
# We recommend deploying the frontend using Vercel for a seamless experience.
# Vercel offers a generous free tier and will automatically handle building
# the TailwindCSS assets.
#
# --- Recommended Method: Vercel Git Integration ---
#
# 1. Push your repository to GitHub, GitLab, or Bitbucket.
# 2. Go to your Vercel dashboard (https://vercel.com/dashboard).
# 3. Click "Add New..." -> "Project".
# 4. Import your Git repository.
# 5. Vercel will automatically detect that it's a static site with a build step.
#    It should configure the following settings for you:
#    - Framework Preset: Other
#    - Build Command: `npm run build:css`
#    - Output Directory: `frontend` (IMPORTANT: You may need to set the Root Directory to 'frontend' and leave Output Directory as default)
#
#    The best configuration on Vercel is:
#    - Root Directory: `frontend`
#    - Build Command: `npm install && npm run build:css`
#    - Output Directory: `.` (or leave blank, as assets are in the root of the frontend dir)
#
# 6. Click "Deploy". Your site will be live in a few moments.
#
# --- Alternative Method: Vercel CLI ---
#
# If you prefer to deploy from the command line, you can use the Vercel CLI.
#
# 1. Install the Vercel CLI:
#    npm install -g vercel
#
# 2. Log in to your Vercel account:
#    vercel login
#
# 3. Navigate to the root of the repository and run the deployment command.
#    You'll need to link the project to a Vercel project first.
#
#    vercel link
#
# 4. Deploy the project:
#    # This command deploys the project to production.
#    vercel --prod
#
#    You will be prompted for settings. Use the same settings as above.
#
echo "This script is a guide. Please follow the instructions above to deploy the frontend."
echo "The recommended method is using Vercel's Git integration."
exit 0
