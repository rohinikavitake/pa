# def create_cube(n):
#     result=[]
#     for x in range (n):
#         result.append(x**3)
#     return result
# print(create_cube(10))


def Create_cube(n):
    for x in range (10):
        yield (x**3)
    print(x)

