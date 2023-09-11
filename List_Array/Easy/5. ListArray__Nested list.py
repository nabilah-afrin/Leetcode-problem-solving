#Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
n=int(input())
result=[],grade=[]
for i in range(n):
    name=input()
    mark=float(input())
    result.append([name,mark])
    grade.append(mark)   
grade=sorted(set(grade))  
name=[]
for val in result:
    if grade[1]==val[1]:
        name.append(val[0])
    name.sort()
for nm in name:
    print(nm)
