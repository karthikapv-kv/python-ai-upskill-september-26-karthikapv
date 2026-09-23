from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api.routers.journal_routes import router as journal_router

app = FastAPI(title="Journal API")

# Allow a frontend served from a different origin to call this API.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(journal_router)


@app.get("/")
def read_root():
    """Landing route confirming the API is running."""
    return {"message": "Journal API is running 🚀"}
