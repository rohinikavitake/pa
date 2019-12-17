# def gen_fib (n):
#     a=1
#     b=1
#     for i in range(n):
#         yield a
#         a,b=b,a+b
# for number in gen_fib(10):
#     print(number)


# def generator():
#     for x in range (3):
#         yield (x)
#for number in generator():
  #  print(number)
#genrator object
# g=generator()
# print(next(g))
# print(next(g))
# print(next(g))

import random
def random_number(low,high,n):
    for i in range(n):
        yield random.randint(low,high)
for number in random_number(1,10,12):
    print(number)

