from fastapi import HTTPException, APIRouter, Depends
from database import SessionLocal
from sqlalchemy.orm import Session
import schemas, models, crud


Routes = APIRouter()


# Función para crear una sesión de base de datos-Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@Routes.post("/kingdoms", response_model=schemas.Kingdom)
async def create_kingdoms(kingdom: schemas.KingdomCreate, db: Session = Depends(get_db)):
    result = crud.create_kingdom(db, kingdom)
    return result