from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,scoped_session
from contextlib import contextmanager


DATABASE_URL = "sqlite:///users.db"

engine = create_engine(DATABASE_URL,connect_args={'check_same_thread': False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# SessionLocal = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

def get_db():
    db = SessionLocal()
    print(">>>getting db",db)
    try:
        yield db
    finally:
        db.close()