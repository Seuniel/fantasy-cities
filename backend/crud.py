import models, schemas
from sqlalchemy.orm import Session

def create_kingdom(db: Session, kingdom: schemas.KingdomCreate):
    db_kingdom = models.Kingdoms(**kingdom.dict())
    db.add(db_kingdom)
    db.commit()
    db.refresh(db_kingdom)
    return db_kingdom