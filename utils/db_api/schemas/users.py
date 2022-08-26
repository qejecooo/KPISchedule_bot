from sqlalchemy import Column, Integer, String, sql
from utils.db_api.db_gino import BaseModel


class User(BaseModel):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    group = Column(String)

    query: sql.Select
