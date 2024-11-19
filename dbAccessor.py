from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base

USER_NAME='root'
PASSWORD='okazaki'
HOST='localhost:3306'
DATABASE='addres'

#url = 'mysql+pymysql://root:okazaki@localhost:3306/addres?charset=utf8'
url = 'mysql+pymysql://{}:{}@{}/{}?charset=utf8'.format(USER_NAME, PASSWORD, HOST, DATABASE)
#Base.metadata.create_all(bind=engine)

# エンジン設定：mysql+pymysqlを使用
engine = create_engine(url, pool_recycle=10)
Base = declarative_base()

# Sessionの作成
Session = sessionmaker(bind=engine)
session = Session(
  autocommit = False,
  autoflush = True,
  bind = engine
)

# modelで使用する
Base = declarative_base()
#Base.query = session.query_property()