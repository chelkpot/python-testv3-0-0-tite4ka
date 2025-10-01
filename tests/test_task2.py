import io, sys
from tasks.task2 import solve

def run_io(input_data: str) -> str:
    old_in, old_out = sys.stdin, sys.stdout
    sys.stdin, sys.stdout = io.StringIO(input_data), io.StringIO()
    try:
        solve()
        return sys.stdout.getvalue().strip()
    finally:
        sys.stdin, sys.stdout = old_in, old_out

def test_case1():
    assert run_io("137\n") == "2 17"

def test_case2():
    assert run_io("2879\n") == "23 59"

def test_case3():
    assert run_io("1511\n") == "1 11"

def test_case4():
    assert run_io("608862\n") == "19 42"
