import os
if os.path.exists("democreatefile.txt"):
    os.remove("democreatefile.txt")
else:
    print("The file does not exist")
