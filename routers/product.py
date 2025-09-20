from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from models.schema import ArtistSchema, CustomerSchema
from models.models import Artist as ArtistModel, Customer as CustomerModel
from data.db import sessionLocal


router = APIRouter(prefix="/products", tags=["products"])

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/artists", summary="Get all artists", response_model=list[ArtistSchema])
async def get_artist(db: Session = Depends(get_db)):
    try:
        db_artists = db.scalars(select(ArtistModel)).all()

        if not db_artists:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='No se encuentran artistas en la base de datos'
            )
        return [ArtistSchema.model_validate(artist) for artist in db_artists]
    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f'Error: {e}'
        )
    
@router.get('/customer', 
           summary="Get all customer", 
           response_model=list[CustomerSchema])
async def get_customer(db: Session = Depends(get_db)):
    try:
        db_customer = db.scalars(select(CustomerModel).where(CustomerModel.country == 'Brazil')).all()
        if not db_customer:
            raise HTTPException(
                status_code= status.HTTP_422_UNPROCESSABLE_CONTENT
                detail="No se pudo realizar la consulta"
            )
        return [CustomerSchema.model_validate(customer) for customer in db_customer]
    except SQLAlchemyError as e_sql:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail=f'Error: {e_sql}'
        )
