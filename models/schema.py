from pydantic import BaseModel, ConfigDict, Field
from typing import List, Dict, Optional

class ArtistSchema(BaseModel):
    artist_id : int = Field(alias="artist_id")
    name: Optional[str] = Field(None, alias="name")
    model_config = ConfigDict(from_attributes=True,
                              populate_by_name=True
                              )

class AlbumSchema(BaseModel):
    album_id: int = Field(alias="albun_id")
    title: Optional[str] = Field(None,alias="title")
    artist_id:int = Field(alias='artist_id')
    model_config = ConfigDict(from_attributes=True,
                              populate_by_name=True
                              )

class CustomerSchema(BaseModel):
    customer_id: int
    first_name: Optional[str] = Field(None, alias='first_name')
    last_name: Optional[str] = Field(None,alias='last_name')
    company: Optional[str] = Field(None, alias='company')
    address : Optional[str] = Field(None, alias='address')
    city : Optional[str] = Field(None, alias='city')
    state : Optional[str] = Field(None, alias='state')
    country : Optional[str] = Field(None, alias='country')
    postal_code : Optional[str] = Field(None, alias='postal_code')
    phone : Optional[str] = Field(None, alias='phone')
    fax : Optional[str] = Field(None, alias='fax')
    email : Optional[str] = Field(None, alias='email')
    support_rep_id : Optional[int] = Field(None,alias='support_rep_id')
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True
    )