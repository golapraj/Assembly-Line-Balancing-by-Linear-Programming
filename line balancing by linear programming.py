import random
import math

TASK = [[], [1], [1], [2], [3], [3], [4, 5, 6], [7]]
TASKTIME = [34.6,24.3,29,89,53.9,12,43.7,46.3]
PREDECESSOR = []
SUCCESSOR = []
E =[]
L = []
MACHINE = 5#input("Enter no machine(>minimum integer theoritical value): ")

CYCLETIME = 90#input("Enter cylce time(>largest task time): ")


tsk = 8#input("How many tasks? ")
'''
for i in range(tsk):
    temp = []
    print "Task ",i+1
    time = input("Time: ")
    TASKTIME.append(time)
    pres=input("How many predecessors? ")
    for j in range(pres):
        print "Predecessors ",j+1
        p = input()
        
        temp.append(p)
    TASK.append(temp)
'''
#predecessors   
for i in range(tsk):
    temp = TASK[i]
    for j in TASK[i]:
        temp = temp + PREDECESSOR[j-1]
    tmp = set(temp)
    pred = list(tmp)
    PREDECESSOR.append(pred)
z=0
for i in PREDECESSOR:
    total = TASKTIME[z]
    for j in i:
        total = total + TASKTIME[j-1]
    total = (1.0*total)/CYCLETIME
    E.append(int(math.ceil(total)))
    z = z + 1

#Successors
for i in range(tsk):
    suc = []
    for j in range(tsk-1,-1,-1):
        for k in TASK[j]:
            if(k==i+1):
                suc.append(j+1)
    SUCCESSOR.append(suc)

SUC = SUCCESSOR[:]

for i in range(tsk-1,-1,-1):
    tmp = SUCCESSOR[i]
    for j in SUCCESSOR[i]:
        tmp = tmp + SUCCESSOR[j-1]
    tmp = list(set(tmp))
    SUCCESSOR[i]=tmp
z=0
for i in SUCCESSOR:
    total = TASKTIME[z]
    for j in i:
        total = total + TASKTIME[j-1]
    total = (1.0*total)/CYCLETIME
    L.append((MACHINE+1)-int(math.ceil(total)))
    z = z + 1



print "Task i\tImmediate predecessor\tti\tEi\tLi"
print "------\t---------------------\t--\t--\t--"  
for i in range (tsk):
    print i+1,"\t",TASK[i],"\t\t\t",TASKTIME[i],"\t",E[i],"\t",L[i]
print "!Objective Function"
print "!Minimize the work station number"
print "MIN",
for i in range(MACHINE):
    print "S%d"%(i+1),
    if(i<MACHINE-1):
        print " +",
print "\nSUBJECT TO"

print "!Constraints"
print "!Assignment Constraint"
for i in range(tsk):
    for j in range(E[i],L[i]+1):
        print "t%d%d"%(i+1,j),
        if (j<L[i]):
            print "+",
    print " = 1\n"

print "!Cycle time constraint"
for i in range(MACHINE):
    z=0
    for j in range(tsk):
        if L[j]>=i+1 and E[j] <= i+1:
            if(z>0):
                print "+",
            print "%.1ft%d%d"%(TASKTIME[j],j+1,i+1),
            z=2
    print " <= ",CYCLETIME,"\n"

print "!Precedence Constraint"
for i in range(tsk):
    for j in SUC[i]:
        for k in range(E[i],L[i]+1):
            print "%dt%d%d"%(k,i+1,k),
            if (k<L[i]):
                print "+",
        for l in range(E[j-1], L[j-1]+1):
            print " - %dt%d%d"%(l,j,l),
        print " <= 0\n",

print "\n!Machine Utilization constraint"
tt=0
for i in range(MACHINE):
    z=0
    h=0
    for j in range(tsk):
        if L[j]>=i+1 and E[j] <= i+1:
            h=h+1
            tt=tt+1
            if(z>0):
                print "+",
            print "t%d%d"%(j+1,i+1),
            z=2
    print " - %dS%d <= 0\n"%(h,i+1)

print "\n!Earlier Machine Utilization constraint"
for i in range(MACHINE):
    for j in range(i+1,MACHINE):
        if(i!=j):
            print "S%d - S%d >=0"%(i+1,j+1)

print "END"
print "INT %d"%(tt+MACHINE)



        
