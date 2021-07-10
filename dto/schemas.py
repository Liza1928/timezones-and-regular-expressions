from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class BirthdayCreate(BaseModel):
    fio: str
    birthday:Optional[datetime]
    birthday_timezone: str
    residence_timezone: str
