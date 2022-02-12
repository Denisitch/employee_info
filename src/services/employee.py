from typing import List, Optional

from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from .. import tables
from ..database import get_session
from ..models.employee import EmployeePosition, EmployeeCreate, EmployeeUpdate


class EmployeeService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def _get(self, employee_id: int) -> tables.Employee:
        employee = self.session.query(tables.Employee).filter_by(id=employee_id).first()
        if not employee:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return employee

    def get_list(
        self, position: Optional[EmployeePosition] = None
    ) -> List[tables.Employee]:
        query = self.session.query(tables.Employee)
        if position:
            query = query.filter_by(position=position)
        employee = query.all()
        return employee

    def get(self, employee_id: int) -> tables.Employee:
        return self._get(employee_id)

    def create(self, employee_data: EmployeeCreate) -> tables.Employee:
        employee = tables.Employee(**employee_data.dict())
        self.session.add(employee)
        self.session.commit()
        return employee

    def update(
        self, employee_id: int, employee_data: EmployeeUpdate
    ) -> tables.Employee:
        employee = self._get(employee_id)
        for field, value in employee_data:
            setattr(employee, field, value)
        self.session.commit()
        return employee

    def delete(self, employee_id: int):
        employee = self._get(employee_id)
        self.session.delete(employee)
        self.session.commit()
