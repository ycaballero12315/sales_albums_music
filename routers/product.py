from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session
from models.db_schema import ArtistSchema, CustomerSchema
from models.models import Artist as ArtistModel, Customer as CustomerModel
from data.db import sessionLocal
from routers.auth import get_current_user

router = APIRouter(prefix="/products", tags=["products"])

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/artists", summary="Get all artists", response_model=list[ArtistSchema])
async def get_artist(db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    
    db_artists = db.scalars(select(ArtistModel)).all()
    if not db_artists:
        from fastapi import HTTPException, status
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No se encontraron artistas en la base de datos."
        )
    return [ArtistSchema.model_validate(artist) for artist in db_artists]
    
@router.get('/customer', 
           summary="Get all customer", 
           response_model=list[CustomerSchema])
async def get_customer(db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    db_customer = db.scalars(select(CustomerModel).where(CustomerModel.country == 'Brazil')).all()
    if not db_customer:
        from fastapi import HTTPException, status
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No se encontraron customer en la base de datos."
        )
    return [CustomerSchema.model_validate(customer) for customer in db_customer]
   