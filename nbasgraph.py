"""nbas grapher. outputs a graphviz representation of the file."""

import os
import out

filename = ""

while filename == "" or not os.path.exists(filename) and os.path.isfile(filename):
    filename = input("file: ")

out.stdout("digraph h {")

with open(filename, "r") as rf:
    lf = rf.readlines()
    for index, item in enumerate(lf):
        print(str(index) + "  [label = \"" + item.replace("\n", "") + "\"]")
    for index, item in enumerate(lf):
        if item.startswith("jmp "):
            print(str(index) + "->" + item.split(" ")[1])
        if item.startswith("jif "):
            line = item.split(" ")
            print(str(index) + "->" + line[4])
            print(str(index) + "->" + str(index + 1))
        else:
            print(str(index) + "->" + str(index + 1))
        