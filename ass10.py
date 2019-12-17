string="This is Cyber sucess"
def upper_lower(string):
    d={"upper":0,"lower":0}
    for character in string:
        if character.isupper():
              d["upper"]+=1
        elif character.islower():
              d["lower"]+=1
        else:
            pass
    print("no of uppercase letters in string",d["upper"])
    print("no of lowercase letters in string",d["lower"])
print(upper_lower("This is Cyber sucess"))