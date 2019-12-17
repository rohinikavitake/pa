#print(__name__)
#print("first module name{}".format(__name__))


def fun():
    print("Function in one.py")
#print("Toplevel in one.py")
if __name__=="__main__":
    print("one.py is being run directily")
else:
    print("one.py has being imported")

