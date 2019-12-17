import  re


text="This is pune , pune is in maharastra"
print(re.search("pune",text))
print(re.findall("pune",text))


phase="What is your email,it is hello@gmail.com"
split_trem="@"
print(re.split('@',phase))

phrase="The  rain in pune"
print(re.sub("\s","g",phrase))


#represtation syntax
# text_phrase='sdsd....ssssddd....sdddd....dsds....dsss....sddd'
# sd*,sd+,


phrase1="This is string! But it has punctuation. how can we remove it?"
x=re.findall('[^ ! . ?]+',phrase1)
print(x)


pharse="This is an example sentance. Lets see if we can find letters"
print(re.findall('[a-z]+',pharse))
print(re.findall('[A-Z]+',pharse))
print(re.findall('[a-z,A-Z]+',pharse))
print(re.findall('[A-Z][a-z]+',pharse))
