from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

MYSQL_USER=os.getenv("MYSQL_USER","root")
MYSQL_PASSWORD=os.getenv("MYSQL_PASSWORD","rootpassword")
MYSQL_HOST=os.getenv("MYSQL_HOST","db")
MYSQL_PORT=os.getenv("MYSQL_PORT","3306")
MYSQL_DATABASE=os.getenv("MYSQL_DATABASE","fastapi_db")

DATABASE_URL=f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}"


print(DATABASE_URL)    
##connection

engine=create_engine(DATABASE_URL,
  echo=True,
  pool_pre_ping=True
)

##session
SessionLocal = sessionmaker(autoflush=False, autocommit= False, bind=engine)

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

##base
Base = declarative_base()
