import importlib.util
from pathlib import Path

file_path = (
    Path(__file__).resolve().parent.parent
    / "code"
    / "02_largest_of_three.py"
)

spec = importlib.util.spec_from_file_location(
    "largest_program", file_path
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.largest_of_three(10, 25, 15) == 25
assert module.largest_of_three(5, 2, 8) == 8
assert module.largest_of_three(20, 30, 10) == 30
assert module.largest_of_three(7, 7, 3) == 7

print("All test cases passed.")