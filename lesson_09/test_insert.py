from sqlalchemy import text


def test_insert(db_connection, insert, delete):
    with db_connection.connect() as connection:
        connection.execute(insert, {"new_subject_title": "QA"})
        check_sql = text("SELECT subject_title "
                         "FROM subject "
                         "WHERE subject_title = :title")
        result = connection.execute(check_sql, {"title": "QA"}).fetchone()
        assert result is not None
        connection.execute(delete, {"subject_title": "QA"})
        after_delete = connection.execute(check_sql,
                                          {"title": "QA"}).fetchone()
        assert after_delete is None
