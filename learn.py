"""
str_1 = "Hello World"
res = ""

for s in str_1:
    if s == "o":
        res = res + "a"
    elif s == "l":
        res = res + "e"
    else:
        res = res + s
print(res)
"""

"""
a = 0
b = 1
print(a)
print(b)
for i in range(20):
    if b < 89:
        a = a + b
        print(a)
        a, b = b, a
"""

"""
# Трикутник Паскаля
N = int(input())
P = []

for i in range(N+1):
    row = [1] * (i+1)
    for j in range(i+1):
        if j != 0 and j != i:
            row[j] = P[i-1][j-1] + P[i-1][j]

    P.append(row)

for r in P:
    print(r)
"""


