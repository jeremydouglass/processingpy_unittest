import tests

def setup():
    tests.run() # run all tests
    
def draw():
    pass

def keyPressed():
    if key == 't':
        tests.run() # run all tests
    elif key == 's':
        tests.run(tests.TestStringMethods) # run specific tests
