import fileinput
import glob
import os
from os.path import dirname

module_path = dirname(__file__)
os.chdir(module_path)


expected = [
    "11,74,59:21.7",
    "11,74,59:22.5",
    "14,25,59:21.4",
    "18,16,59:21.7",
    "20,41,59:22.5",
    "22,87,59:21.7",
    "22,87,59:22.3",
    "23,68,59:22.4",
    "27,105,59:21.7",
    "32,42,59:22.5",
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
