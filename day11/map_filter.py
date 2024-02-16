def abc(a):
    a()
    print("hello")

def hi():
    print("hi")

abc(hi)


def makeFry():
    return '🍳'
def makeTaco():
    return '🌮'
def makePizza():
    return '🍕'

def cooking(x):
    a = x()
    print(f"{a} 요리중")

cooking(makePizza)
cooking(makeFry)



