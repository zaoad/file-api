# main.py
import secure
from api.issue_token_routes import router as issue_token_router
from api.process_file_routes import router as process_file_router
from config import settings
from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from utils.log_function import setup_logging

setup_logging()

app = FastAPI(
    title=settings.project_name,
    description=settings.project_description,
)

csp = secure.ContentSecurityPolicy().default_src("'self'").frame_ancestors("'none'")
hsts = secure.StrictTransportSecurity().max_age(31536000).include_subdomains()
referrer = secure.ReferrerPolicy().no_referrer()
cache_value = secure.CacheControl().no_cache().no_store().max_age(0).must_revalidate()
x_frame_options = secure.XFrameOptions().deny()

secure_headers = secure.Secure(
    csp=csp,
    hsts=hsts,
    referrer=referrer,
    cache=cache_value,
    xfo=x_frame_options,
)
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["POST", "PUT"],
    allow_headers=["*"],
)


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    message = str(exc.detail)

    return JSONResponse({"message": message}, status_code=exc.status_code)