try:
     number=int(input("enter number: "))
     print(number)
except:
     print("invaid number")
try:
    value=10/0
except:
    print("sorry number is not divied by zero")

while True:
     try:
         number=int(input("enter number"))

     except:
         print("please provid number")
         continue
     else:
         print("yes thank you")
         break