import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Employee(Base):
    __tablename__ = "employee"

    id = sa.Column(sa.Integer, primary_key=True)
    first_name = sa.Column(sa.String)
    last_name = sa.Column(sa.String)
    patronymic = sa.Column(sa.String, nullable=True)
    position = sa.Column(sa.String)
    date_of_birth = sa.Column(sa.Date)
    phone_number = sa.Column(sa.String)
