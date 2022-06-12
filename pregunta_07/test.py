import fileinput
import glob
import os
from os.path import dirname

module_path = dirname(__file__)
os.chdir(module_path)


expected = [
    "A,2,4",
    "A,2,5",
    "A,2,5",
    "A,2,5",
    "A,3,3",
    "A,3,4",
    "A,3,5",
    "A,3,6",
    "B,2,3",
    "B,2,5",
    "B,2,5",
    "B,3,5",
    "B,3,6",
    "B,4,4",
    "B,4,6",
    "C,4,3",
    "C,4,3",
    "C,4,4",
    "C,4,5",
    "C,4,6",
    "D,2,3",
    "D,2,3",
    "D,2,4",
    "D,2,6",
    "D,3,3",
    "D,4,5",
    "E,2,3",
    "E,2,3",
    "E,2,3",
    "E,2,3",
    "E,2,4",
    "E,2,6",
    "E,3,3",
    "E,3,3",
    "E,3,5",
    "E,3,5",
    "E,3,6",
    "E,3,6",
    "E,4,3",
    "E,4,6",
]

if os.path.isdir("output"):
    os.system("rm -rf output")

os.system("docker run -v $PWD:/workspace jdvelasq/pig:classroom")

assert os.path.isdir("output") is True

result = []
with fileinput.input(files=glob.glob("output/*")) as f:
    for line in f:
        line = line.replace("\n", "")
        result.append(line)

for expected_line, result_line in zip(expected, result):
    assert (
        expected_line == result_line
    ), f"Expected: {expected_line}\nGot: {result_line}"
