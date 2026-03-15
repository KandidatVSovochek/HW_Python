from sqlalchemy import text


def test_delete(db_connection, insert, delete):
    with db_connection.connect() as connection:
        connection.execute(insert, {"new_subject_title": "Абракадабра"})
        check_sql = text("SELECT subject_title "
                         "FROM subject "
                         "WHERE subject_title = :title")
        result = connection.execute(check_sql,
                                    {"title": "Абракадабра"}).fetchone()
        assert result is not None
        connection.execute(delete, {"subject_title": "Абракадабра"})
        after_delete = connection.execute(check_sql,
                                          {"title": "Абракадабра"}).fetchone()
        assert after_delete is None
