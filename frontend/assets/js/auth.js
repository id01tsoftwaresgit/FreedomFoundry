// --- IMPORTANT: CONFIGURE YOUR SUPABASE CREDENTIALS HERE ---
// You can find these in your Supabase project's API settings.
const SUPABASE_URL = 'YOUR_SUPABASE_URL';
const SUPABASE_KEY = 'YOUR_SUPABASE_ANON_KEY';
// -------------------------------------------------------------


// --- Supabase Client Initialization & Auth Logic ---

let supabase;

function checkSupabaseCredentials() {
    if (!SUPABASE_URL || !SUPABASE_KEY || SUPABASE_URL.startsWith('YOUR_') || SUPABASE_KEY.startsWith('YOUR_')) {
        const message = "CRITICAL ERROR: Supabase credentials are not configured. Please edit /frontend/assets/js/auth.js and replace the placeholder values.";
        console.error(message);

        // Display a prominent error on the page to ensure the user sees it.
        const errorDiv = document.createElement('div');
        errorDiv.innerHTML = `
            <h2 style="font-size: 1.2rem; font-weight: bold; margin-bottom: 10px;">Configuration Needed</h2>
            <p>${message}</p>
        `;
        errorDiv.style.backgroundColor = '#fef2f2';
        errorDiv.style.color = '#991b1b';
        errorDiv.style.padding = '20px';
        errorDiv.style.border = '2px solid #f87171';
        errorDiv.style.borderRadius = '8px';
        errorDiv.style.margin = '20px';
        document.body.prepend(errorDiv);

        return false;
    }
    return true;
}

function initializeSupabase() {
    if (checkSupabaseCredentials()) {
        supabase = window.supabase.createClient(SUPABASE_URL, SUPABASE_KEY);
        return true;
    }
    return false;
}

// Universal logout function
async function handleLogout() {
    if (!supabase) return;
    const { error } = await supabase.auth.signOut();
    if (error) {
        console.error('Error logging out:', error);
    } else {
        // Clear local storage related to the app
        localStorage.removeItem('selectedVenture');
        localStorage.removeItem('freedomfoundry_api_keys');
        window.location.href = '/login.html';
    }
}

// Auth state management
document.addEventListener('DOMContentLoaded', () => {
    if (initializeSupabase()) {
        const isAppPage = window.location.pathname.startsWith('/app/');
        const isLoginPage = window.location.pathname.endsWith('/login.html');

        supabase.auth.onAuthStateChange(async (event, session) => {
            if (event === 'SIGNED_OUT' || !session) {
                if (isAppPage) {
                    window.location.href = '/login.html';
                }
            } else if (event === 'SIGNED_IN') {
                if (isLoginPage) {
                    window.location.href = '/app/';
                }
            }
        });

        // Initial check in case the listener doesn't fire right away
        setTimeout(async () => {
            const { data: { session } } = await supabase.auth.getSession();
            if (!session && isAppPage) {
                window.location.href = '/login.html';
            } else if (session && isLoginPage) {
                window.location.href = '/app/';
            }
        }, 100);
    }
});
