"""nbas grapher. outputs a graphviz representation of the file."""

import os
import out

filename = ""

while filename == "" or not os.path.exists(filename) and os.path.isfile(filename):
    filename = input("file: ")

out.stdout("digraph h {")

with open(filename, "r") as rf:
    lf = rf.readlines()
    out.stdaout("start -> 0")
    for index, item in enumerate(lf):
        out.stdaout(str(index) + "  [label = \"" + item.replace("\n", "") + "\"]")
    for index, item in enumerate(lf):
        if item.startswith("jmp "):
            out.stdaout(str(index) + "->" + str(int(item.split(" ")[1]) - 1))
        elif item.startswith("jif "):
            line = item.split(" ")
            out.stdaout(str(index) + "->" + str(int(line[4]) - 1))
            out.stdaout(str(index) + "->" + str(index + 1))
        elif item.startswith("vjm"):
            out.stdaout(str(index) + "-> \"?\"")
        else:
            out.stdaout(str(index) + "->" + str(index + 1))
out.stdaout("}")
        