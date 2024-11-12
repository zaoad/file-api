# main.py

from fastapi import FastAPI
from routes.file_service_routes import api_router
from utils.log_function import setup_logging
from fastapi.middleware.cors import CORSMiddleware
from configs.config import settings
import logging

setup_logging()

app = FastAPI(
    title=settings.project_name,
    description=settings.project_description,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["POST", "PUT"],
    allow_headers=["*"],
)

logging.info("Registering API routes.")
app.include_router(api_router)

if __name__ == "__main__":
    import uvicorn
    logging.info("Starting the application.")
    uvicorn.run(app, host="0.0.0.0", port=8000)
