class student():
    name = " "
    age = 0
    marks = 0 

students=[]

s2=student();
s1=student();
s1.name = "Harsh"
s1.age = int(input("enter age of "+s1.name +" "))
s1.marks = 89
students.append(s1)
s2.name = "Arsh"
s2.age = 22
s2.marks = 89
students.append(s2)
#taking iput from user for 3 4 5 student

for i in range(3,5):
    si=student()
    si.name=input("enter name of "+ str(i) +" Student ")
    si.age=int(input("enter age of " +si.name +" "))
    si.marks=int(input("enter marks of "+ si.name +" "))
    students.append(si)

for i in range(4):
    print(students[i].name,students[i].marks,students[i].age)


