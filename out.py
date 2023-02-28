curfile = ""

def stdout(out : str, nl : bool = True):
    fw = open(curfile, "w")
    if nl:
        fw.write(out + "\n")
    else:
        fw.write(out)
    fw.close()
def stdaout(out : str, nl : bool = True):
    fa = open(curfile, "a")
    if nl:
        fa.write(out + "\n")
    else:
        fa.write(out)
    fa.close()
def stdin():
    fr = open(curfile, "r")
    return fr.read()