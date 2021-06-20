### GroupBy
将 `相同的且连续的` 字符分组.

&nbsp;  
现象
```shell script

text = 'AAAABBBCCDAABBB'
s = [(k, list(g)) for k, g in groupby(text)]
print(s)
# [('A', ['A', 'A', 'A', 'A']),
#  ('B', ['B', 'B', 'B']),
#  ('C', ['C', 'C']),
#  ('D', ['D']),
#  ('A', ['A', 'A']),
#  ('B', ['B', 'B', 'B'])]


s = {k: list(g) for k, g in groupby(text)}
print(s)
# {'A': ['A', 'A'],
#  'B': ['B', 'B', 'B'],
#  'C': ['C', 'C'],
#  'D': ['D']}


text = 'AAAABBBCCD'
s = [(k, list(g)) for k, g in groupby(text)]
print(s)
# [('A', ['A', 'A', 'A', 'A']),
#  ('B', ['B', 'B', 'B']),
#  ('C', ['C', 'C']),
#  ('D', ['D'])]


s = {k: list(g) for k, g in groupby(text)}
print(s)
# {'A': ['A', 'A', 'A', 'A'], 
#  'B': ['B', 'B', 'B'], 
#  'C': ['C', 'C'], 
#  'D': ['D']}

```