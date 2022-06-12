import fileinput
import glob
import os
from os.path import dirname

module_path = dirname(__file__)
os.chdir(module_path)


expected = [
    "1971-07-08,08,8,jue,jueves",
    "1974-05-23,23,23,jue,jueves",
    "1973-04-22,22,22,dom,domingo",
    "1975-01-29,29,29,mie,miercoles",
    "1974-07-03,03,3,mie,miercoles",
    "1974-10-18,18,18,vie,viernes",
    "1970-10-05,05,5,lun,lunes",
    "1969-02-24,24,24,lun,lunes",
    "1974-10-17,17,17,jue,jueves",
    "1975-02-28,28,28,vie,viernes",
    "1969-12-07,07,7,dom,domingo",
    "1973-12-24,24,24,lun,lunes",
    "1970-08-27,27,27,jue,jueves",
    "1972-12-12,12,12,mar,martes",
    "1970-07-01,01,1,mie,miercoles",
    "1974-02-11,11,11,lun,lunes",
    "1973-04-01,01,1,dom,domingo",
    "1973-04-29,29,29,dom,domingo",
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
