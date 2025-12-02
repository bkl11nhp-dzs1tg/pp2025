#n = int(input("number of students "))
students=[{'id': '1', 'name': 'linh', 'dob':'1-1','course':'101'},{'id': '2', 'name': 'huy', 'dob':'2-2','course':'102'}]
courses=[{'id':'101', 'name':'mat'}, {'id':'102', 'name':'ict'}]
t=""
n=len(students)
m=len(courses)
'''
for i in range (n):
    #a = input("id, name, dob of student ").split()
    students.append(a)
#m = int(input("number of courses "))
courses=[]

for i in range (m):
    b = input("id, name of course ").split()
    courses.append(b)
    '''
for _ in range(m):
    c = input("select course id ")
    for i in range (m):
        if c==courses[i]["id"]:
            p=input("enter mark "+courses[i]["name"]+": ")
            courses[i]["mark"]=p
    for i in range (n):
        if c==students[i]["course"]:
            t+="mark of student "+students[i]["name"]+": "+courses[i]["mark"]+"\n"
print(t)        
