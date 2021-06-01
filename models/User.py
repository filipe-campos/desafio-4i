from sqlalchemy import Column, Integer, String, Date
from db.base_class import Base


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    cpf = Column(Integer, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    full_name = Column(String, index=True)
    birthday = Column(Date)
    cep = Column(Integer)
    street = Column(String)
    neighborhood = Column(String)
    city = Column(String)
    state = Column(String)
