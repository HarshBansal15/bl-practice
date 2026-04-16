#school report card 
class student():
    school="New School of Learning"
    name=""
    phy=0
    chem=0
    maths=0
   
students=[]

for i in range (3):
    s=student()
    students.append(s)

for i in range (3):
    students[i].name=input("Enter name: ")
    students[i].phy=int(input(f"Enter phy Marks out of 50 for student {i+1} "))
    students[i].chem=int(input(f"Enter chem Marks out of 50 for student {i+1} "))
    students[i].maths=int(input(f"Enter maths Marks out of 50 for student {i+1} "))
    
    Total=students[i].phy+students[i].maths+students[i].chem
    print(f"{student.school}-class XI - {students[i].name}")
    print("-"*70)
    print(f"| {"Subject":^10} | {"Total Marks":^10} | {"Marks Obtained":^10} | {"Percentage":^10} | ")
    print(f"| {"Physics":^10} | {"50":^10} | {students[i].phy:^10} | {(students[i].phy/50)*100:^10.2f} | ")
    print(f"| {"Chemistry":^10} | {"50":^10} | {students[i].chem:^10} | {(students[i].chem/50)*100:^10.2f} | ")
    print(f"| {"Maths":^10} | {"50":^10} | {students[i].maths:^10} | {(students[i].maths/50)*100:^10.2f} | ")
    print(f"| {"Total":^10} | {"150":^10} | {Total:^10} | {(Total/150)*100:^10.2f} | ")
    print("\n"*3)






    