#IBM-Hack Allotment Code
#Controller

#Assuming origin and destination between 1 and 10
#Distance randomly generated and stored in atemporary array for now
import random
import math
from queue import Queue
import UserModel as um
from operator import attrgetter

q=[]
n_users=int(input("Enter number of users to deal with:"))

if n_users<=10:
    bufferSize=5
else:
    bufferSize=10

n_origin=10
n_destination=10
distance=[]
d=[]

'''def comparator(a:um.User, b:um.User):
    if a.distance!=b.distance:
        if a.distance>b.distance:
            return 1
        elif a.distance<b.distance:
            return -1
        else :
            return 0
    else:
        if a.origin>b.origin:
            return 1
        elif a.origin<b.origin:
            return -1
        else:
            return 0'''

def totDistance(org,dest):
    total=0
#    print(org," ",dest)
    for i in range(org,dest+1):
        total+=d[i]
    return total

def assignDistance():
    for i in range(n_origin):
        col=[]
        for j in range(n_destination):
            if i<j:
                col.append(totDistance(i,j))
            elif i>j:
                col.append(totDistance(j,i))
            else:
                col.append(0)
        distance.append(col)
        
def printDistanceMatrix():
    for i in range(n_origin):
        for j in range(n_destination):
            print(distance[i][j],end='\t')
        print()

def insert():
    d.append(0)
    for i in range(1,n_destination):
        d.append(random.uniform(10,50))
    
    assignDistance()
        
    for i in range(n_users):
        org=int(random.uniform(0,n_destination-1))
        dest=int(random.uniform(org+1,n_destination))
        dist=distance[org][dest]
        q.append(um.User(org,dest,dist))
        
def display():
    #printDistanceMatrix()
    for user in q:
        #user=q.pop(0)
        print(user.origin,' ',user.destination,' ',user.distance)
        
def allocateBus():
    #buffRequired=int(math.ceil(n_users/bufferSize))
    finalList=[]
    while len(q)>0:
        buffer=[]
        for i in range(bufferSize):
            if(len(q)>0):
                user=q.pop(0)
                buffer.append(user)
        #sorted(buffer,key=um.User.comparator)
        s=sorted(buffer,key=attrgetter('origin'))     # sort on secondary key
        sorted(s, key=attrgetter('distance'))   
        #print(s)
        finalList.append(s)
        
    for li in finalList:
        for i in li:
            print(i)

insert()
#printDistanceMatrix()
print("Origin\tDestination\tDistance")
display()
print("Sorted List first Originwise then Distancewise:")
allocateBus()
