import io, sys
from tasks.task3 import solve

def run_io(input_data: str) -> str:
    old_in, old_out = sys.stdin, sys.stdout
    sys.stdin, sys.stdout = io.StringIO(input_data), io.StringIO()
    try:
        solve()
        return sys.stdout.getvalue().strip()
    finally:
        sys.stdin, sys.stdout = old_in, old_out

def test_case1():
    assert run_io("125\n") == "3"

def test_case2():
    assert run_io("43\n") == "5"

def test_case3():
    assert run_io("10000000\n") == "100000"
