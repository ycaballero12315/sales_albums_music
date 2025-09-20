from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Dict, Optional
from routers import product

app = FastAPI()


app.include_router(product.router)
# --- IGNORE ---    


