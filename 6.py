x = list(range(10))
print(x)
x[:0] = x[-3:]
del x[-3:]
x[-3:] = []
print(x)

y = x
y[4] = 100
print(x)
print(y)