from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from urllib.parse import quote_plus


MYSQL_USER='root'
MYSQL_PASSWORD=quote_plus("Harsha123")
MYSQL_HOST='localhost'
MYSQL_PORT='3306'
MYSQL_DATABASE='fastapi_db'

DATABASE_URL=f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}"


print(DATABASE_URL)    
##connection

engine=create_engine(DATABASE_URL)

##session
SessionLocal = sessionmaker(autoflush=False, autocommit= False, bind=engine)

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

##base
Base= declarative_base()
