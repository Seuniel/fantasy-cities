from database import Base, engine
from sqlalchemy import Column, ForeignKey, Boolean, Integer, String

from sqlalchemy.orm import relationship



class Kingdoms(Base):
    __tablename__ = "kingdoms"
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    kingdom_name = Column(String(50), index=True, nullable=False)
    source = Column(String(50), nullable=False)
    description = Column(String(255))
    city = relationship("Cities", back_populates="kingdom_id")

class Cities(Base):
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    city_name = Column(String(50), index=True, nullable=False)
    lacation = Column(String(255))
    language = Column(String(50))
    kingdom_id = Column(Integer, ForeignKey("kingdoms.id"), nullable=False)
    Kingdom = relationship("Kingdoms", back_populates="cities")




Base.metadata.create_all(engine)