class Foo:
    # Khai bao o dang public
    name = "Foo"
    # Khai bao o dang public
    def getName(self):
        print(self.name)

# goi thanh phan ngoai Class
print(Foo().name) # Foo
Foo().getName() # Foo

class Bar(Foo):
    pass

#test
Bar().getName() # Foo
