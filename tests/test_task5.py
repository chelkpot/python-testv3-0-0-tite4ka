import io, sys
from tasks.task5 import solve

def run_io(input_data: str) -> str:
    old_in, old_out = sys.stdin, sys.stdout
    sys.stdin, sys.stdout = io.StringIO(input_data), io.StringIO()
    try:
        solve()
        return sys.stdout.getvalue().strip()
    finally:
        sys.stdin, sys.stdout = old_in, old_out

def test_case1():
    assert run_io("3721\n") == "1:02:01"

def test_case2():
    assert run_io("5000\n") == "1:23:20"

def test_case3():
    assert run_io("55408\n") == "15:23:28"

def test_case4():
    assert run_io("48147\n") == "13:22:27"
