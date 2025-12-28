students=[
    ("Riya",85),
    ("Aman",72),
    ("Neha",48),
    ("Vikram",95),
    ("Sara",67),
    ("Karan",43),
    ("Pooja",88),
    ("Ramesh",59),
    ("Tina",49),
    ("Ali",78)
]

def top_students(n):
    sort=sorted(students,key=lambda x:x[1],reverse=True)
    print(sort[0:n])
top_students(10)
sum=0
for i in students:
    sum+=i[1]
avg=sum/10
print("average of all the students is",avg)
f=open('remedial.txt','w')

for i in students:
    if(i[1]<50):
        f.write(f"{i[0]} \n")
f.close()
file=open("remedial.txt","r")
content=file.read()
print(content)
file.close()