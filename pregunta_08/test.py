import fileinput
import glob
import os
from os.path import dirname

module_path = dirname(__file__)
os.chdir(module_path)


expected = [
    "(a,aaa),5",
    "(a,bbb),7",
    "(a,ccc),13",
    "(a,ddd),13",
    "(a,eee),7",
    "(a,fff),10",
    "(a,ggg),8",
    "(a,hhh),8",
    "(a,iii),7",
    "(a,jjj),10",
    "(b,aaa),4",
    "(b,bbb),7",
    "(b,ccc),5",
    "(b,ddd),7",
    "(b,eee),5",
    "(b,fff),8",
    "(b,ggg),4",
    "(b,hhh),7",
    "(b,iii),7",
    "(b,jjj),5",
    "(c,aaa),5",
    "(c,bbb),4",
    "(c,ccc),12",
    "(c,ddd),9",
    "(c,eee),6",
    "(c,fff),8",
    "(c,ggg),7",
    "(c,hhh),7",
    "(c,iii),8",
    "(c,jjj),8",
    "(d,aaa),4",
    "(d,bbb),6",
    "(d,ccc),7",
    "(d,ddd),5",
    "(d,eee),6",
    "(d,fff),8",
    "(d,ggg),6",
    "(d,hhh),4",
    "(d,iii),9",
    "(d,jjj),8",
    "(e,aaa),3",
    "(e,bbb),8",
    "(e,ccc),9",
    "(e,ddd),7",
    "(e,eee),7",
    "(e,fff),9",
    "(e,ggg),4",
    "(e,hhh),4",
    "(e,iii),8",
    "(e,jjj),3",
    "(f,aaa),8",
    "(f,bbb),10",
    "(f,ccc),13",
    "(f,ddd),17",
    "(f,eee),11",
    "(f,fff),11",
    "(f,ggg),9",
    "(f,hhh),10",
    "(f,iii),10",
    "(f,jjj),12",
    "(g,aaa),3",
    "(g,bbb),3",
    "(g,ccc),6",
    "(g,ddd),5",
    "(g,eee),4",
    "(g,fff),5",
    "(g,ggg),4",
    "(g,hhh),3",
    "(g,iii),4",
    "(g,jjj),6",
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
