from sqlalchemy import create_engine, false
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create a sqlite engine instance
engine = create_engine("sqlite:///student.db")

# Create a DeclarativeMeta instance
Base = declarative_base()

# Create SessionLocal class from sessionmaker factor
SessionLocal=sessionmaker(autocommit=false,bind=engine)