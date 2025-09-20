from fastapi import FastAPI
from middleware.errors import error_handling_middleware
from routers import product

app = FastAPI()

app.middleware('http')(error_handling_middleware)
app.include_router(product.router)
# --- IGNORE ---    


