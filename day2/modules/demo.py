import person as p
import platform
from person import name

print(p.name["firstName"])

x = platform.system()
print(x)

y = dir(platform)
print(y)

print(name["firstName"], name['lastName'])