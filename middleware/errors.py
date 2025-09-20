from fastapi import Request
from fastapi.responses import JSONResponse
from sqlalchemy.exc import SQLAlchemyError
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def error_handling_middleware(request: Request, call_next):
    try:
        response = await call_next(request)
        return response
    except SQLAlchemyError as e:
        logger.error(f"Error en la base de datos: {str(e)}")
        return JSONResponse(
            status_code=500,
            content={"detail": "Error en la base de datos, contacte al administrador."},
        )
    except Exception as e:
        logger.error(f"Error inesperado: {str(e)}")
        return JSONResponse(
            status_code=500,
            content={"detail": "Error interno del servidor."},
        )