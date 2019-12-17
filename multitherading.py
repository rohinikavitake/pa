class Hello():
    def run(self):
        for i in range(5):
            print("Hello")


class Hi():
    def run(self):
        for i in range(5):
            print("Hi")

t1=Hello()
t2=Hi()
t1.run()
t2.run()


from threading import*
class Hello(Thread):
     def run(self):
       for i in range(5):
          print("Hello")

class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")

t1=Hello()
t2=Hi()
t1.start()
t2.start()


#to increase the time of exeution if we for 100times we import sleep form time
from time import sleep
from threading import *
class Hello(Thread):
    def run(self):
        for i in range(100):
            print("Hello")
            sleep(1)

class Hi(Thread):
    def run(self):
        for i in range(100):
            print("Hi")
            sleep(1)

t1=Hello()
t2=Hi()
t1.start()
#t2.start()
sleep(0.2)
t2.start()





