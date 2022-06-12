import fileinput
import glob
import os
from os.path import dirname

module_path = dirname(__file__)
os.chdir(module_path)
expected = [
    "B,2015-09-23,1",
    "B,2017-03-09,2",
    "B,2017-11-19,9",
    "B,2017-03-10,10",
    "B,2018-06-15,12",
    "B,2017-06-05,15",
    "C,2017-02-18,5",
    "C,2015-02-01,8",
    "D,2017-11-11,3",
    "D,2016-07-03,4",
    "D,2017-11-03,7",
    "D,2017-09-27,13",
    "D,2017-08-25,14",
    "E,2015-11-28,6",
    "E,2015-08-02,11",
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
