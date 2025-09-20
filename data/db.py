from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from psycopg2 import connect
import os
from dotenv import load_dotenv

load_dotenv()

USER = os.getenv('USER')
PASS = os.getenv('PASS')
DB = os.getenv('DB')
HOST = os.getenv('HOST')
PORT = os.getenv('PORT')

DATABASE_URL = f'postgresql://{USER}:{PASS}@{HOST}:{PORT}/{DB}'
engine = create_engine(DATABASE_URL)
sessionLocal = sessionmaker(autoflush=False, bind=engine, autocommit=False)

