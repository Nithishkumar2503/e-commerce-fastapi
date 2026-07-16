from fastapi import FastAPI
import logging
from app.api.brands import router as brand_router

app = FastAPI(
    title="E-Commerce API",
    description="Backend API for E-commerce platform.",
    version="1.0.0",
)

# Configure logging
logger = logging.getLogger(__name__)


@app.get("/")
def root():
    return {"message": "Welcome to E-Commerce API"}


app.include_router(brand_router)
