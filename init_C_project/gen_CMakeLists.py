import re
import os
import sys

def gen_the_file(prjName):
    lines = open("./CMakeLists_template.txt", "r").readlines()
    dst_file = os.path.join(prjName, "CMakeLists.txt")
    dst_file_handle = open(dst_file, "w")
    for line in lines:
        parse_pattern = re.compile("template")
        result = parse_pattern.sub(prjName, line)
        dst_file_handle.write(result)

gen_the_file(sys.argv[1])        
    
