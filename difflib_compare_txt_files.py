import difflib
import filecmp

file1 = "MDDC20230518-MDEC.txt"
file2 = "MDDC20230126.txt"

with open(file1, "r") as f1, open(file2, "r") as f2:
    diff = difflib.unified_diff(f1.readlines(), f2.readlines())

    for line in diff:
        print(line)