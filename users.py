from sqlalchemy import Table, Column, Integer, String, MetaData, select
from dbAccessor  import Base

class Users(Base):
    __tablename__ = 'users'
    __table_args__ = {
        'comment': 'ユーザー情報のマスターテーブル'
    }

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    title = Column('title', String(100), nullable=False)
    body = Column('body', String(1000), nullable=False)

