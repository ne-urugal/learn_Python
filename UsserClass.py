class Users:
    def __init__(self, name, age):
        self.name = name
        self.age = age

User_1 = Users(input('Enter your name: '), int(input('Enter your age: ')))

def printingUser():
    return User_1.name


