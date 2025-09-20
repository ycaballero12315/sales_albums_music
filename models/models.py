from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class Artist(Base):
    __tablename__ = 'artist'
    artist_id = Column('artist_id',Integer, primary_key=True, index = True)
    name = Column('name',String)

class Album(Base):
    __tablename__ = "Album"
    AlbumId = Column(Integer, primary_key=True, index = True)
    Title = Column(String)
    ArtistId = Column(Integer)

class Track(Base):
    __tablename__ = "Track"
    TrackId = Column(Integer, primary_key=True, index=True)
    Name = Column(String)
    AlbumId = Column(Integer)
    MediaTypeId = Column(Integer)
    GenreId = Column(Integer)
    Composer = Column(String)
    Milliseconds = Column(Integer)
    Byte = Column(Integer)
    UnitPrice = Column(Integer)

class Customer(Base):
    __tablename__ = 'Customer'
    CustomerId = Column(Integer, primary_key=True, index=True)
    FirstName = Column(String)
    LastName = Column(String)
    Company = Column(String)
    Address = Column(String)
    City = Column(String)
    State = Column(String)
    Country = Column(String)
    PostalCode = Column(String)
    Phone = Column(String)
    Fax = Column(String)
    Email = Column(String)
    SupportRepId = Column(Integer)