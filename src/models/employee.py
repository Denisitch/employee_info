from datetime import date
from enum import Enum
from typing import Optional

from pydantic import BaseModel


class EmployeePosition(str, Enum):
    MANAGER = "manager"
    ENGINEER = "engineer"
    DEVELOPER = "developer"
    DIRECTOR = "director"


class EmployeeBase(BaseModel):
    first_name: str
    last_name: str
    patronymic: Optional[str]
    position: EmployeePosition
    date_of_birth: date
    phone_number: str


class Employee(EmployeeBase):
    id: int

    class Config:
        orm_mode = True


class EmployeeCreate(EmployeeBase):
    pass


class EmployeeUpdate(EmployeeBase):
    pass
