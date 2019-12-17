x="sneha"
list=[letters for letters in x]
print(list)
x=[numbers for numbers in range (1,10)]
print(x)
y=[numbers**2 for numbers in range (1,10)]
print(y)
x=[num for num in range (1,51)if num%3==0]
print(x)
x=[num**2 for num in range (1,51)if num%3==0]
print(x)
celcius=[0,15,30,40]
farenheit=[9/5*temp+32 for temp in celcius]
print(farenheit)

x=[num for num in range (1,100)if num%2==0]
print(x)
string="print everyword in this sentence that has an even numbers of letters"
for word in string. split():
  if len (word)%2==0:
    print(word+"is even")
string="this is cyber success"
for word in string.split():
    if len (word)%2!=0:
        print(word+ "is odd")




string="sam prints only the words that start with s in this sentence"
list=string.split()
for s in list:
    if s.startswith("s"):
     print(s)