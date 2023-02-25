def stdout(out : str, nl : bool = True):
    fw = open("out.xdot", "w")
    if nl:
        fw.write(out + "\n")
    else:
        fw.write(out)
    fw.close()
def stdaout(out : str, nl : bool = True):
    fa = open("out.xdot", "a")
    if nl:
        fa.write(out + "\n")
    else:
        fa.write(out)
    fa.close()
def stdin():
    fr = open("out.xdot", "r")
    return fr.read()
    fr.close()