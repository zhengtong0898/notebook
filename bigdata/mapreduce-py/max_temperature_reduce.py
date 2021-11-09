import sys


last_key = None
max_val = -sys.maxsize


for line in sys.stdin.readlines():
    key, val = line.strip().split("\t")

    if last_key and last_key != key:
        print("%s\t%s" % (last_key, max_val))
        last_key = key
        max_val = int(val)
    else:
        last_key = key
        max_val = max(max_val, int(val))

if last_key:
    print("%s\t%s" % (last_key, max_val))
