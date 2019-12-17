
#Inheritance
# class Chef():
#      def make_chicken(self):
#         print("The chef makes chichen")
#      def make_salad(self):
#         print("The chef makes salad")
#      def make_spl_dish(self):
#         print("The chef makes spl dish")
# mychef=Chef()
# print(mychef.make_chicken())
# class Chinesechef(Chef):
#      def make_fried_rice(self):
#              print("The chef makes fried rice")
# mychinesechef=Chinesechef()
# print(mychinesechef.make_chicken())





#Polymorphism
# class Dog():
#     def __init__(self,name):
#         self.name=name
#     def speak(self):
#         return self.name+"says woof"
# class Cat():
#     def __init__(self,name):
#         self.name=name
#     def speak(self):
#         return self.name+"says meow"
# niko=Dog("niko")
# felix=Cat("filo")
# print(niko.speak())
# print(felix.speak())



# polymorphism using for loops
# class India():
#    def capital(self):
#         print("Delhi is a capital of India")
#    def language(self):
#         print("hindi is primary language")
#    def type(self):
#         print("india is develeping country")
#
# class USA():
#    def capital(self):
#         print("US is a capital of India")
#
#    def language(self):
#             print("English is primary language")
#
#    def type(self):
#             print("USA is develeped country")
# india=India()
# usa=USA()
# for country in(india,usa):
#  country.capital()
#  country.language()
#  country.type()





#Polymorphism with inheritance

# class Bird:
#    def intro(self):
#         print("There are many types of birds")
#    def flight(self):
#         print("most of birds can fly but some cannot")
# class Sparrow(Bird):
#    def flight(self):
#         print("sparrow can fly")
# class Ostrich(Bird):
#    def flight(self):
#         print("ostrich cannot fly")
# bird=Bird()
# spa=Sparrow()
# ost=Ostrich()
# bird.intro()
# bird.flight()
# spa.intro()
# spa.flight()
# ost.intro()
# ost.flight()

#Encapsulation



# String Representation
# print("The strring is {}".format("inserted"))
# print("The {} {} {}".format("quick","brown","fox"))
# print("The {0} {1} {2}".format("quick","brown","fox"))
#
# print("Hello his name is {}". format("Jose"))
# name="Jose"
# age=24
# print(f"hello his name is {name}")
# print(f"{name} is {age} years old")





#create a bank account class that has two attribute 1.owner 2.balance and two method 1.deposite 2.withdrowl as an added requirement withdrowl may not
# access available balance

# class Bankac():
#     def __init__(self,owner,balance):
#        self.owner=owner
#        self.balance=balance
#
#     def deposite(self,dept_amt):
#         self.dept_amt=dept_amt
#         self.balance=self.balance+dept_amt
#         print(f"Added{dept_amt} to the balance")
#
#     def withdrowl(self,wd_amt):
#       #####self.wd.amt=wd_amt
#       if self.balance>wd_amt:
#        self.balance=self.balance-wd_amt
#        print("withdrowl accepted ")
#       else:
#        print("you doesnot having fund")
#     def __str__(self):
#        return f"owner:{self.owner}\nbalance:{self.balance}"
# mybank=Bankac("sam",500)
# mybank.deposite(100)
# mybank.withdrowl(50)
# print(mybank.__str__())




#specilemethods
# class Book():
#    def __init__(self,title,author,pages):
#       self.title=title
#       self.author=author
#       self.pages=pages
#
#    def __str__(self):
#      return f"{self.title} by {self.author} having {self.pages}"
#    def __len__(self):
#      return self.pages
# b=Book("python rocks","van-Rossum",200)
# print(b)
