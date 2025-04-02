from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


DB_SESSION_URL = "/" #TODO: Database complete URL to come here
engine = create_engine(DB_SESSION_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush = False, bind = engine)
def get_db():
    """Database connection"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()