# hello.py

def hello():
    print("Hello world!")

def greet(who="Students and professionals"):
    "Create a greeting"
    return "{}, good evening!".format(who)

if "__main__" == __name__:
    greet()
