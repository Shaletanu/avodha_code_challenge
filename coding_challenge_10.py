class Computer:
    def __init__(self, name, bitsize, weight) :
        self.name = name
        self.bitsize = bitsize
        self.weight = weight

    def getspecs(self):
        self.name = input("Enter name of company: ")
        self.bitsize = input("Enter bitsize: ")


class Desktop(Computer):
    def getdesk(self):
        self.weight = input("Enter weight of Desktop:")

    def printdesk(self):
        print("Company name: ", self.name)
        print("Bitsize: ", self.bitsize)
        print("Weight of desktop: ", self.weight)


class Laptop(Computer):
    def getlap(self):
        self.weight = input("Enter weight of Laptop:")

    def printlap(self):
        print("Company name: ", self.name)
        print("Bitsize: ", self.bitsize)
        print("Weight of laptop: ", self.weight)


obj = Desktop('', '', '')
obj.getspecs()
obj.getdesk()
obj.printdesk()
obj1 = Laptop('', '', '')
obj1.getspecs()
obj1.getlap()
obj1.printlap()
