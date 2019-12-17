name=["umesh","vishal","rohini","shivani"]
print(name)
print(name[0])
name.insert(0,11)
print(name)
name.append(77)
print(name)
name.remove(11)
print(name)
name.pop(2)
print(name)
#name.sort()
#sprint(name)
name.reverse()
print(name)

tup=(11,2,33,4,5)
print(tup)
print(tup[1])

#user input
'''x=int(input("enter first no: "))
y=int(input("enter rno: "))
z=x+y
print(z)'''


#student information
'''name=input("enter name: ")
rno=(input("enter rno: "))
marks=int(input("enter sub marks"))
if marks>=40:
    print("student is pass",marks)
else:
    print("student is fail",marks)'''

'''num=int(input("enter any no: "))
if num%5==0 or num%10==0:
    print("num is div by five and ten",num)
else:
    print("num is not div by five and ten")'''

'''ab=input("enter any char: ")
if ab=='a'or ab=='e'or ab=='i'or ab=='o'or ab=='u' or ab=='A'or ab=='E'or ab=='I'or ab=='O'or ab=='U':
    print("character is vowel: ")
else:
    print("character is consonent: ")'''

'''#Even numbers
n=0
while n<=10:
    print(n)
    n+2'''

'''n1=0
while n1<=20:
    print(n1)
    n1+=1'''

'''n1=0
while n1<=10:
     print(n1)
     n1+=1'''

'''m1=0
while m1<=10:
    if m1==5:
        break
    else:
        print(m1)
    m1+=1'''

'''m=0
while m<=10:
    if m==7:
         m+=1
         continue
    else:
         print(m)
         m+=1'''

#REverse number
# num1=int(input("enter any no: "))
# #num=123
# rev=0
# while (num1>0):
#     rem=num1%10  #num is divided by 10 and rem store the value in rem.
#     rev=(rev*10+rem)
#     num1=num1//10
# print("Revers",+rev)



# #palindrome number
# num1=int(input("enter any no: "))
# #num=123
# rev=0
# tem=r=num1
# while (num1>0):
#     rem=num1%10
#     rev=(rev*10+rem)
#     num1=num1//10
# if rev==tem:
#     print("number is paildrome",rev)
# else:
#     print("number is not palidrome",rev)

#Armsstrong number
# num=int(input("enter any no:"))
# cubesum=0
# temp=num
# while num>0:
#     rem=num%10
#     cube=rem*rem*rem
#     cubesum=cubesum+cube
# if cubesum == temp:
#     print("number is armstrong",cubesum)
# else:
#     print("number is not armstrong",cubesum)

abc=[1,2,3,'abc','xyz'3.2]
for a in range(1,5):
    print(abc.count(0))