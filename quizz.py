question_prompts=["what colours are apple?\n (a)red\n(b)green\n(c)purple\n\n",
                  "what colour are banana?\n(a)white\n(b)yellow\n(c)teal\n\n",
                  "what colour are starwberry?\n(a)yellow\n(b)red\n(c)red\n\n",
                  ]
class Question():
    def __init__(self,prompts,answer):
        self.prompts=prompts
        self.answer=answer
questions=[
            Question(question_prompts[0],"a"),
            Question(question_prompts[1],"b"),
            Question(question_prompts[2],"b")
]
def run_test(question):
        score=0
        for question in questions:
            answer=input(question.prompts)
            if answer==question.answer:
                score+=1
        #print("you got",score,"out of",len(questions))
        print("you got"+str(score)+"/"+str(len(question_prompts))+"correct")
run_test(questions)




