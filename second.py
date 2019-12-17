import one
#print("Top level in second.py")
one.fun()
if __name__=="__main__":
    print("second.py is being run directly")
else:
    print("second.py is imported")
