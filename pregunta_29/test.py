import fileinput
import glob
import os
from os.path import dirname

module_path = dirname(__file__)
os.chdir(module_path)


expected = [
    "1971-07-08,jul,07,7",
    "1974-05-23,may,05,5",
    "1973-04-22,abr,04,4",
    "1975-01-29,ene,01,1",
    "1974-07-03,jul,07,7",
    "1974-10-18,oct,10,10",
    "1970-10-05,oct,10,10",
    "1969-02-24,feb,02,2",
    "1974-10-17,oct,10,10",
    "1975-02-28,feb,02,2",
    "1969-12-07,dic,12,12",
    "1973-12-24,dic,12,12",
    "1970-08-27,ago,08,8",
    "1972-12-12,dic,12,12",
    "1970-07-01,jul,07,7",
    "1974-02-11,feb,02,2",
    "1973-04-01,abr,04,4",
    "1973-04-29,abr,04,4",
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
