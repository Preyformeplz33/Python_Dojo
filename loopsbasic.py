for i in range(1,151):
    print (i)


for i in range (5,5001):
    if i % 5 == 0:
        print(i)

for i in range(1,101):
    if i % 10 == 0:
        print ("Coding Dojo")
    elif i % 5 == 0:
        print ("coding")
    else: 
        print (i)
    
sum = 0
for i in range(0,500001):    
    if i % 3 == 0:
        sum = sum + i
        
print (sum)

for i in range(2018,0,-4):
    print(i)

lownum = 1
highnum = 33
multi =3

for i in range(lownum,highnum):
    if i % multi == 0 and i != 0:
        print (i)