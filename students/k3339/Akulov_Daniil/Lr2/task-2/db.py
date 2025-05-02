from sqlmodel import SQLModel, Session, create_engine
import os
from dotenv import load_dotenv
load_dotenv()

db_url = os.getenv('LAB1_DB_URL')

engine = create_engine(db_url, echo=True)


def get_session():
    with Session(engine) as session:
        yield session