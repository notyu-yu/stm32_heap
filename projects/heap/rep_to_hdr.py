import sys

file = sys.argv[1].strip();

with open(file, 'r') as f:
    f_str = f.read()
    hdr_str = "#define TESTSTRING \""
    hdr_str += f_str.replace("\n", "\\n")
    hdr_str += '"'
    with open("teststring.h", "w+") as hf:
        hf.write(hdr_str)

print(f'teststring.h created from {file}')
