import sys


last_key = None
max_val = 0


# 这是一个实时流读取和实时排序算法.
# 从当前案例来看它即可以是每个节点上的job, 也可以是汇聚节点上的 combiner.
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
