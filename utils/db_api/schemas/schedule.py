from sqlalchemy import Column, String, sql, Integer
from utils.db_api.db_gino import TimedBaseModel


class Schedule(TimedBaseModel):
    __tablename__ = 'schedule'
    id = Column(Integer, primary_key=True)
    first_lesson = Column(String)
    second_lesson = Column(String)
    third_lesson = Column(String)
    fourth_lesson = Column(String)
    fifth_lesson = Column(String)

    query: sql.Select
