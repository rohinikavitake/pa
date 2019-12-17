secret_word="xyz"
guess=""
guess_limit=3
guess_count=0
out_of_guessess=False

while guess!=secret_word and not (out_of_guessess):
    if guess_count< guess_limit :
       guess=input("enter guess")
       guess_count+=1
    else:
        out_of_guessess =True
    if out_of_guessess:
        print("you lose")
    else:
        print("you win")