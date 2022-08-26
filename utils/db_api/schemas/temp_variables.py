from sqlalchemy import Column, Integer, String, sql
from utils.db_api.db_gino import BaseModel


class TempVariable(BaseModel):
    __tablename__ = 'temp_variables'
    variable = Column(String, primary_key=True)
    value = Column(Integer)

    query: sql.Select
