import fileinput
import glob
import os
from os.path import dirname

module_path = dirname(__file__)
os.chdir(module_path)


expected = [
    "aaa,13",
    "bbb,16",
    "ccc,23",
    "ddd,23",
    "eee,15",
    "fff,20",
    "ggg,13",
    "hhh,16",
    "iii,18",
    "jjj,18",
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
