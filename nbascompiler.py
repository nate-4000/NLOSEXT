import os
import out
out.curfile = "compiled.cnb"

filename = ""

while filename == "" or not os.path.exists(filename) and os.path.isfile(filename):
    filename = input("file: ")
