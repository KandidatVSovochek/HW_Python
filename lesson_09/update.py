from sqlalchemy import text


def test_update(db_connection, insert, delete):
    with db_connection.connect() as connection:
        connection.execute(insert, {"new_subject_title": "QA"})
        check_sql = text("SELECT subject_title "
                         "FROM subject "
                         "WHERE subject_title = :title")
        result = connection.execute(check_sql, {"title": "QA"}).fetchone()
        assert result is not None
        sql = text("UPDATE subject SET subject_id = :subject_id")
        connection.execute(sql, {"subject_id": "17"})
        check_sql_update = text("SELECT subject_id "
                                "FROM subject "
                                "WHERE subject_id = :subject_id")
        result_update = connection.execute(check_sql_update,
                                           {"subject_id": "17"}).fetchone()
        assert result_update is not None
        assert result_update.subject_id == 17
        connection.execute(delete, {"subject_title": "QA"})
        after_delete = connection.execute(check_sql,
                                          {"title": "QA"}).fetchone()
        assert after_delete is None
