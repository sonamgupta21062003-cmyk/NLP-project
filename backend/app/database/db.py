#FastAPI
 #     │
 #     ▼
#chat_service.py
#      │
#      ▼
#crud.py
##      │    ▼
##      │
#      ▼
#SQLite Database

"""
Database Configuration

This modules craeate the SQLALchemy engine,
database sesion , ans Base class.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

#----------------------------------------
# Database URL 
#------------------------------------------

DATABASE_URL = settings.DATABASE_URL

#------------------------------------------
# SQLALchemy
#------------------------------------------

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

# =====================================================
# Session Factory
# =====================================================

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

#=====================================================
# Base Class
#=======================================================

Base = declarative_base()

#=====================================================
#Dependency
#=====================================================

def get_db():
    """
    Create a database session.
    Used by FastAPI dependency injection.
    """

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()