from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session
from models.schema import ArtistSchema
from models.models import Artist as ArtistModel
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
    db_artists = db.scalars(select(ArtistModel)).all()
    return [ArtistSchema.model_validate(artist) for artist in db_artists]
