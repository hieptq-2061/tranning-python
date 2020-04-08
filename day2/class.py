class Person:
    def __init__(this, firstName, lastName):
        this.firstName = firstName
        this.lastName = lastName

    def printFullName(this):
        print(this.firstName + " " + this.lastName)
p = Person("Tran", "Hiep")
p.printFullName()

p.firstName = "Nguyen"
p.printFullName()

del p