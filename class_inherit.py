'''
@author: shuaigao
@file: class_inherit.py
@time: 2021/11/29 10:22
@desc:
'''

class Person(object):
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def eat(self,food):
        print('i am eating %s '%food)

    def drink(self,drinking):
        print('i am drinking %s'%drinking)

    def sleep(self,site):
        print('i am sleeping at %s'%site)

class Student(Person):
    def __init__(self,name,age,gender):
        Person.__init__(self,name,age,gender)

    def study(self,school):
        print('i am studying at %s'%school)

if __name__ == "__main__":
    stu = Student("wang",18,"male")
    stu.study("NO.1 school")