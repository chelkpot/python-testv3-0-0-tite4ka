import io, sys
from tasks.task4 import solve

def run_io(input_data: str) -> str:
    old_in, old_out = sys.stdin, sys.stdout
    sys.stdin, sys.stdout = io.StringIO(input_data), io.StringIO()
    try:
        solve()
        return sys.stdout.getvalue().strip()
    finally:
        sys.stdin, sys.stdout = old_in, old_out

def test_case1():
    assert run_io("5\n") == "6"

def test_case2():
    assert run_io("6\n") == "8"

def test_case3():
    assert run_io("401\n") == "402"

def test_case4():
    assert run_io("163\n") == "164"
