class Person:
    # Constructor: Phuong thuc khoi tao
    def __init__(self, name, age, states, male):
        print("This is Constructor Method")
        self.name = name
        self.age = age
        self.states = states
        self.male = male

    def getName(self):
        print("Name: %s" % (self.name))
    def setName(self, name):
        self.name = name

    def getAge(self):
        print("Age: %s" % (self.age))
    def setAge(self):
        self.age = age

    def getStates(self):
        print("States: %s" % (self.states))
    def setStates(self, states):
        self.states = states

    def getMale(self):
        print("Male: %d" % (self.male))
    def setMale(self, male):
        self.male = male

    # Destructor: Phuong thuc huy
    def __del__(self):
        del self.name, self.age, self.states, self.male

person = Person("Beo Kun", 22, "VietNam", True)

# methods get
person.getName() # Beo Kun
person.getAge() # 22
person.getMale() # False
