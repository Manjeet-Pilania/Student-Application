from sqlalchemy import Column, Integer, String
from database import Base

# Define students class inheriting from Base
class students(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    task = Column(String(256))