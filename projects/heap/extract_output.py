import re

with open("./gdb_out.txt", "r") as f:
    f_str = f.read()
    for line in f_str.split("\n"):
        if "$1" in line:
            print(re.search('".*"', line).group()[1:-1].rstrip("\\n"))
            
