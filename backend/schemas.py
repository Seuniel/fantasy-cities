

from pydantic import BaseModel

class KingdomBase(BaseModel):
    kingdom_name: str
    source: str
    description: str | None = None


class CityBase(BaseModel):
    city_name: str
    location: str
    language: str
    kingdom_id: int

class KingdomCreate(KingdomBase):
    pass

class Kingdom(KingdomBase):
    id: int
    cities: list[CityBase]
    class Config:
        orm_mode = True

class CityCreate(CityBase):
    pass

class City(CityBase):
    id: int
    kingdom: Kingdom
    class Config:
        orm_mode = True
