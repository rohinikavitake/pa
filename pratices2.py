
# function
a=50
def abc():
    global a
    a=10
    print(a)
abc()

def hello():
    print('hello')
hello()

def upadte1(x):
    print(id(x))
    x=8
    print("x= :",x)
a=10
print(id(a))

upadte1(a)
print("a= :",a)


#position
'''def add(a,b):
    c=a+b
    print(c)
add(4,3)
#keyword
def person(name,age):
    print(name)
    print(age)
person(name="xyz",age=29)

#Default
def person(name,age=29):
    print(name)
    print(age)
person(name="xyz")

#variable length
def sum(a,*b):
    c=a
    for i in b:
        c=c+i
        print(c)
sum(3,4,6,7,8)



def person1(name,*data):
    print(name)
    print(data)
person1("umesh",100,23,200,9974646546)



def person2(name,**data):
    print(name)
    for i,j in data.items():
        print(i,j)
person2("umesh",age=29,city="pune",mob=24874842298)


list=[2,4,5,7,10,9,22,67,18]
def count(list):
    even=0
    odd=0
    for i in list:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd
even,odd=count(list)
print("Even : {} and odd :{}".format(even,odd))


a ,b ,c , d =1 ,2 ,3 ,4
global a ,b
def add(a ,b): c=a+b
    print(c)


def sub(a,b):
    c=a-b
    print(c)


#### lambda

def square(a):
    return a*a
result=square(4)
print(result)

f=lambda a:a*a
result=f(5)
print(result)

f=lambda a,b:a+b
result=f(10,20,30)
print(result)

num=[1, 2 ,4, 5, 7, 8, 19 ,1 0,2 0] evens=list ( filter(lambda n:n%2== 0 an d n%5==0,n u m ))
p rint(evens)

# double1=list(map(lambda n:n*2,evens))
# print(double1)
from functools import reduce
double= \

[4,19 , 20, 3,4 ,6]
s um =reduc e (lambda a,b:a+b, do u b le )
print(sum)


num=[1 ,2,3, 4] s=r ed uce( l ambda a,b:a+b,nu m) pr in t(s)





###

y
from c import *
a=10
b=2

c = add( a ,b) print(c )

c=mult(a,b) print(c)



#### c.py


def add(a,b):
    r eturn a+b
def su b (a


,b): return a-b
def mult(a , b)


:
    retu rn a*b'''






