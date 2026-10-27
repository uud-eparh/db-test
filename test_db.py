import psycopg
import pytest
from conftest import get_conn_params


def test_connection_ok(db_conn):
    """Проверяем, что подключение установлено и SELECT 1 работает."""
    with db_conn.cursor() as cur:
        cur.execute("SELECT 1")
        row = cur.fetchone()
    assert row is not None
    assert row[0] == 1


def test_now_query(db_conn):
    """Простейший запрос из ТЗ: select now()."""
    with db_conn.cursor() as cur:
        cur.execute("SELECT now()")
        row = cur.fetchone()
    assert row is not None
    assert row[0] is not None


def test_bad_password_fails():
    """Негативный тест: с неверным паролем подключение падает."""
    bad = get_conn_params()
    bad["password"] = "wrong_password"
    with pytest.raises(psycopg.OperationalError):
        with psycopg.connect(**bad):
            pass