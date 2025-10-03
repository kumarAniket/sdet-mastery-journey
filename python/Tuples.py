t=(1,2,3)
print(type(t))

t=('one',2,3.0)
print(f"Length >> {len(t)}")

t=('a','c','b','a')
print("Index of c >> {}".format(t.index('c')))
print(f"Count of a >> {t.count('a')}")