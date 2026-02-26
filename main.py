from fastapi import FastAPI
from fastapi.responses import RedirectResponse, HTMLResponse

app = FastAPI()

# --- SETTINGS ---
GUMROAD_LINK = "https://happyhappiness.gumroad.com/l/giiipe"
PLATFORM_NAME = "HappyHappiness AI"

@app.get("/", response_class=HTMLResponse)
async def home():
    """A simple professional landing page for your server"""
    return f"""
    <html>
        <head><title>{PLATFORM_NAME}</title></head>
        <body style="font-family: Arial; text-align: center; padding: 50px;">
            <h1>Welcome to {PLATFORM_NAME}</h1>
            <p>Your premier source for AI creation tools.</p>
            <a href="{GUMROAD_LINK}" style="background: #2563eb; color: white; padding: 15px 25px; text-decoration: none; border-radius: 5px;">
                View AI Tools on Gumroad
            </a>
            <br><br>
            <p style="font-size: 0.8em; color: gray;">Processing high-speed tech assets...</p>
        </body>
    </html>
    """

@app.get("/go")
async def redirect_to_gumroad():
    """A quick redirect link for your social media bio"""
    return RedirectResponse(url=GUMROAD_LINK)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
