from typing import List, Optional

from fastapi import APIRouter
from fastapi import Depends
from fastapi import Response
from fastapi import status

from ..models.employee import Employee, EmployeePosition, EmployeeCreate, EmployeeUpdate
from ..services.employee import EmployeeService

router = APIRouter(prefix="/employee")


@router.get("/", response_model=List[Employee])
def get_employee(
    position: Optional[EmployeePosition] = None,
    service: EmployeeService = Depends(),
):
    return service.get_list(position=position)


@router.post("/", response_model=Employee)
def create_employee(
    employee_data: EmployeeCreate, service: EmployeeService = Depends()
):
    return service.create(employee_data)


@router.get("/{employee_id}", response_model=Employee)
def get_employee(
    employee_id: int,
    service: EmployeeService = Depends(),
):
    return service.get(employee_id)


@router.put("/{employee_id}", response_model=Employee)
def update_employee(
    employee_id: int,
    employee_data: EmployeeUpdate,
    service: EmployeeService = Depends(),
):
    return service.update(employee_id, employee_data)


@router.delete("/{employee_id}")
def delete_employee(
    employee_id: int,
    service: EmployeeService = Depends(),
):
    service.delete(employee_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
