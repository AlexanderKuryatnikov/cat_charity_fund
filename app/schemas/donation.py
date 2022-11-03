from datetime import datetime
from pydantic import BaseModel, Extra, PositiveInt
from typing import Optional


class DonationCreate(BaseModel):
    full_amount: PositiveInt
    comment: Optional[str]

    class Config:
        extra = Extra.forbid


class DonationDB(DonationCreate):
    id: int
    create_date: datetime
