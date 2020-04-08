for c in "hello world":
    if c == 'd':
        break
    elif c == 'o':
        continue
    else:
        print(c)
else:
    print("finish!")

for x in range(1,6):
    print(x)

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

