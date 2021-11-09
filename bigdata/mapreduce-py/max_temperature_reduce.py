import sys


last_key = None
max_val = 0


for line in sys.stdin.readlines():
    key, val = line.strip().split("\t")

    # init, set max_val
    if not last_key:
        last_key = key
        max_val = int(val)
        continue

    # same key, choose max val
    if last_key == key:
        last_key = key
        max_val = max(max_val, int(val))
        continue

    # diff key, set max_val
    print("%s\t%s" % (last_key, max_val))
    last_key = key
    max_val = int(val)


if last_key:
    print("%s\t%s" % (last_key, max_val))
