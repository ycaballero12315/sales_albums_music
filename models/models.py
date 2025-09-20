from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Artist(Base):
    __tablename__ = 'artist'
    artist_id = Column('artist_id',Integer, primary_key=True, index = True)
    name = Column('name',String)

class Album(Base):
    __tablename__ = "album"
    AlbumId = Column('album_id',Integer, primary_key=True, index = True)
    Title = Column('title',String)
    ArtistId = Column('artist_id',Integer)

class Track(Base):
    __tablename__ = "track"
    TrackId = Column('track_id',Integer, primary_key=True, index=True)
    Name = Column('name',String)
    AlbumId = Column('album_id',Integer)
    MediaTypeId = Column('media_type_id', Integer)
    GenreId = Column('genre_id', Integer)
    Composer = Column('composer_id', String)
    Milliseconds = Column('milliseconds', Integer)
    Byte = Column('byte', Integer)
    UnitPrice = Column('unit_price', Integer)

class Customer(Base):
    __tablename__ = 'customer'
    customer_id = Column('customer_id',Integer, primary_key=True, index=True)
    first_name = Column('first_name',String)
    last_name = Column('last_name', String)
    company = Column('company', String)
    address = Column('address', String)
    city = Column('city', String)
    state = Column('state', String)
    country = Column('country',String)
    postal_code = Column('postal_code',String)
    phone = Column('phone', String)
    fax = Column('fax',String)
    email = Column('email', String)
    support_rep_id = Column('support_rep_id', Integer)

class Employee(Base):
    __tablename__ = 'employee'
    employee_id = Column('employee_id', Integer, primary_key=True, index=True)
    last_name = Column('last_name', String)
    first_name = Column('first_name', String)
    title = Column('title', String)
    reports_to = Column('reports_to', String)
    birth_date = Column('birth_date', TIMESTAMP)
    hire_date = Column('hire_date', TIMESTAMP)
    address = Column('address', String)
    city = Column('city', String)
    state = Column('state', String)
    country = Column('country', String)
    postal_code = Column('postal_code', String)
    phone = Column('phone', String)
    fax = Column('fax', String)
    email = Column('email', String)