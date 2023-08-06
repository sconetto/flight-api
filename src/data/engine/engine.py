from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# TODO: Inject during runtime the database name and location
SQLALCHEMY_DATABASE_URL = "sqlite:///./flight.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    """
    Simple function to yield a session (cursor) to the local database

    :returns: a yielded connection (cursor) to the binded database
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
