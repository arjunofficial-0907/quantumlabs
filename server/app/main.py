from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware

from sqlalchemy.exc import SQLAlchemyError
from app.tokens.token_model import RefreshToken

# ==========================================
# DATABASE
# ==========================================

from app.database.connection import (
    engine,
    Base
)

# ==========================================
# CONFIG
# ==========================================

from app.core.config import settings

# ==========================================
# LOGGER
# ==========================================

from app.core.logger import logger

# ==========================================
# EXCEPTIONS
# ==========================================

from app.core.exceptions import (
    sqlalchemy_exception_handler,
    generic_exception_handler
)

# ==========================================
# MIDDLEWARE
# ==========================================

from app.middleware.error_handler import (
    ErrorHandlerMiddleware
)

from app.middleware.request_logger import (
    RequestLoggerMiddleware
)

# ==========================================
# IMPORT MODELS
# ==========================================

from app.models.project_model import Project
from app.models.service_model import Service
from app.models.lead_model import Lead
from app.models.user_model import User
from app.audit.audit_model import AuditLog

# ==========================================
# IMPORT ROUTES
# ==========================================

from app.routes.project_routes import (
    router as project_router
)

from app.routes.service_routes import (
    router as service_router
)

from app.routes.contact_routes import (
    router as contact_router
)

from app.routes.auth_routes import (
    router as auth_router
)

from app.routes.dashboard_routes import (
    router as dashboard_router
)

from app.uploads.upload_routes import (
    router as upload_router
)

# ==========================================
# FASTAPI APP
# ==========================================

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="Production Backend API for Quantum Labs"
)

# ==========================================
# LOGGER STARTUP
# ==========================================

logger.info("Quantum Labs API Starting...")

# ==========================================
# RATE LIMITER
# ==========================================

limiter = Limiter(
    key_func=get_remote_address
)

app.state.limiter = limiter

app.add_exception_handler(
    RateLimitExceeded,
    lambda request, exc: {
        "success": False,
        "message": "Too many requests"
    }
)

app.add_middleware(
    SlowAPIMiddleware
)

# ==========================================
# GLOBAL ERROR MIDDLEWARE
# ==========================================

app.add_middleware(
    ErrorHandlerMiddleware
)

app.add_middleware(
    RequestLoggerMiddleware
)

# ==========================================
# GLOBAL EXCEPTION HANDLERS
# ==========================================

app.add_exception_handler(
    SQLAlchemyError,
    sqlalchemy_exception_handler
)

app.add_exception_handler(
    Exception,
    generic_exception_handler
)

# ==========================================
# CORS
# ==========================================

origins = [
    settings.FRONTEND_URL
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

# ==========================================
# ROUTES
# ==========================================

app.include_router(project_router)

app.include_router(service_router)

app.include_router(contact_router)

app.include_router(auth_router)

app.include_router(dashboard_router)

app.include_router(upload_router)

# ==========================================
# ROOT
# ==========================================

@app.get("/")
def home():

    logger.info("Root endpoint called")

    return {
        "success": True,
        "message": "Quantum Labs API Running"
    }

# ==========================================
# HEALTH CHECK
# ==========================================

@app.get("/api/health")
def health():

    return {
        "success": True,
        "status": "healthy",
        "app": settings.APP_NAME,
        "version": settings.APP_VERSION
    }