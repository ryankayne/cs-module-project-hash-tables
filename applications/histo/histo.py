d = {}
def function(s):
    f = open(s, "r")
    f.read()
    for x in f:
        if x not in d:
            d[x] = "#"
        if x in d:
            d[x] += "#"
    print(d)

function("robin.txt")