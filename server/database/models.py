from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.sqltypes import Boolean, DateTime

Base = declarative_base()


class User(Base):
    __tablename__ = "Users"
    UserID = Column(Integer, primary_key=True, autoincrement=False)
    NameSurname = Column(String)
    Email = Column(String)
    Password = Column(String)
    Active = Column(Boolean)
    UpdateDate = Column(DateTime)
    UserType = Column(String)

