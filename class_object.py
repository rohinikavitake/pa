# class Student():
#     def __init__(self,name,major,gpa):
#         self.name =name
#         self.major=major
#         self.gpa=gpa
#
#
# st=Student("nikhil ,commerce", 2.3)
# print(st.name)
# print(st.major)
# print(st.gpa)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


person = Person("John", 36)

print(person.name)
print(person.age)








#class function
class Student():
    def _init__(self,name,major,gpa):
      self.name=name
      self.major=major
      self.gpa=gpa
    def is_on_probution(self):
        if self.gpa >3.5:
            return True
        else:
            return False
student2=Student("nikhil","commerce", 3.4)
print(student2.is_on_probution())

#area of circle
# class Circle():
#     pi=3.14
#     def __init__(self,radius=2):
#         self.radius=radius
#     def circumference(self):
#          print(2*self.pi*self.radius)
# mycircle=Circle()
# mycircle.circumference()

#distance of line
# class Line():
#
#
#     def __init__(self,co1,co2):
#         self.co1=co1
#         self.co2=co2
#     def distance(self):
#         x1,y1= self.co1
#         x2,y2= self.co2
#         return ((x2-x1)**2+(y2-y1)**2)*0.5
#     def slope(self):
#         x1,y1= self.co1
#         x2,y2= self.co2
#         return((y2-y1)/(x2-x1))
# c1=(4,5)
# c2=(5,6)
# myline=Line(c1,c2)
# print(myline.distance())
# print(myline.slope())
#

#volume of cylinder and surface of area
class Vol():
    pi=3.14
    def __init__(self,radius=2,height=4):
        self.radius=radius
        self.height=height
    def volumeofcylinder(self):
        print(self.pi*self.radius*self.radius*self.height)
    def surface_of_area(self):
        print(2*self.pi*self.radius*self.radius+2*self.pi*self.radius*self.height)
myvol=Vol()
myvol.volumeofcylinder()
myvol.surface_of_area()





