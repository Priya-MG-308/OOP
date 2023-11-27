#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Employee():
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
    def details(self):
        print("Name is ",self.name,"\nAge is ",self.age,"\nSalary is ",self.salary)
        
a=Employee("Ram",34,1000000)

a.details()


# In[2]:


class Student():
    def __init__(self):
        self.name="Ram"
        self.age=34
        self.grade="A"
a=Student()
print(a.name,a.age,a.grade)


# In[3]:


class Employee():
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def details(self):
        print("Length is ",self.length,"\nBreadth is ",self.breadth)   
        
a=Employee(3,4)

a.details()


# In[4]:


class birthdayboy():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def birthday(self):
        print("\n----------------------\nName is ",self.name,"\n\nAge was ",self.age)   
        self.age=self.age+1
        print("It became ",self.age) 
        
        
a=birthdayboy("Ram",4)
a.birthday()

b=birthdayboy("Shyam",7)
b.birthday()


# In[5]:


class Songs():
    def __init__(self,lyrics):
        self.lyrics=lyrics
    def sing_me_a_song(self):
        for i in self.lyrics:
            print(i)
song=['Whenever, wherever','We are meant to be together','I will be there and you will be near','Thats the deal my dear.']  
a=Songs(song)
a.sing_me_a_song()


# In[16]:


class room():
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        print("Area is : ",self.l*self.b)
r=room(22,23)
r.area()


# In[18]:


class Dog():
    def __init__(self,name,size,breed,dob):
        self.name=name
        self.size=size
        self.breed='unknown'
        self.dob='unknown'
    def bark(self):
        print("woof!")
        
    def get_name(self):
        print("Name is ",self.name)
    
    def set_name(self):
        n=input("Enter name: ")
        self.name=n
        
a=Dog('Snoopy',44,'Golden Retriever','13/05/2000')
print(a.bark())
a.set_name()
a.get_name()


# In[ ]:




