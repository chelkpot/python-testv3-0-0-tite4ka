import pytest

def test_score():
    # Запускаем все тесты
    result = pytest.main(["-q", "tests/test_task1.py", "tests/test_task2.py", 
                          "tests/test_task3.py", "tests/test_task4.py", "tests/test_task5.py",
                          "--disable-warnings"])
    # result == 0 если все тесты прошли
    assert result == 0
