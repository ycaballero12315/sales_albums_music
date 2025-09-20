from pydantic import BaseModel, ConfigDict, Field
from typing import List, Dict, Optional

model_config = ConfigDict(from_attributes=True,
                              populate_by_name=True
                              )

class ArtistSchema(BaseModel):
    artist_id : int = Field(alias="artist_id")
    name: Optional[str] = Field(None, alias="name")
    model_config

class AlbumSchema(BaseModel):
    album_id: int = Field(alias="albun_id")
    title: Optional[str] = Field(None,alias="title")
    artist_id:int = Field(alias='artist_id')
    model_config
