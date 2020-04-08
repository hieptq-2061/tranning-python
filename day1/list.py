a = ["hello", "world"]
print(a[1])

b = ["hello", "world"]
b[0] = "world"
print(b[0])

c = ["hello", "world"]
for value in c:
    print(value)

if "world" in c:
    print("exist")
print(len(c))

c.append("add")
print(c)

c.remove("add")
print(c)

c.insert(2, "add")
print(c)

c.pop()
print(c)

del c[0]
print(c)

