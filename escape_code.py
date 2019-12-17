import re
str="The rain in pune"
#x=re.findall('\AThe',str)
#print(x)
# if (x):
#     print("Yes,string start with specified character")
# else:
#     print("Not start with specified character")



x=re.findall (r"ain\b",str)
#print(x)
if (x):
    print("Yes, there is match")
else:
    print("No match")


string="This is a string with some numbers 1233 and a symbol # hashtag"
#x=re.findall(r"\d+",string)
#x=re.findall(r"\D+",string)
#x=re.findall(r"\s+",string)
#x=re.findall(r"\S+",string)
#x=re.findall(r"\w+",string)
# x=re.findall(r"\W+",string)
# print(x)



# def lenofstring():
#     count=0
#     for i in string:
#         count+=1
#     return count
# print(lenofstring("pune")



a=["Aakah","pooja","a","b"]
#for i in range enumerate(a):
#print(i)
for i in range (len (a)):
      print(i,a[i])


