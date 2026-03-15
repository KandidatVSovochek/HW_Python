import pytest
from dotenv import load_dotenv
import os
from sqlalchemy import create_engine, text


load_dotenv()


@pytest.fixture(scope="session")
def db_connection():
    db_connection = os.getenv("base_string")
    db = create_engine(db_connection)
    return db


@pytest.fixture(scope="session")
def insert(db_connection):
    connection = db_connection.connect()
    sql = text("INSERT INTO subject (\"subject_title\")"
               "VALUES (:new_subject_title)")
    connection.execute(sql, {"new_subject_title": "QA"})
    return sql


@pytest.fixture(scope="session")
def delete():
    sql = text("DELETE FROM subject WHERE subject_title = :subject_title")
    return sql
