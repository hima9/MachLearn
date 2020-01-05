
# coding: utf-8

# In[ ]:

import random
import sys
import math
from collections import defaultdict
import numpy as np

def dot_product(lst1,lst2):
	refw=lst1
	refx=lst2
	dp=0
	for j in range(0,cols,1):
		dp+=refw[j]*refx[j]
	return dp
	
#read data file
datafile=sys.argv[1]
f=open(datafile)
data=[]
i=0
l=f.readline()
while(l!=''):
    k=l.split()
    l2=[]
    for j in range(0,len(k),1):
        l2.append(float(k[j]))
    data.append(l2)
    l=f.readline()
    
rows=len(data)
cols=len(data[0])
f.close()
#read label 
labelfile=sys.argv[2]
f=open(labelfile)
trainlabels={}
n=[]
n.append(0)
n.append(0)
l=f.readline()
while(l!=''):
	k=l.split()
	trainlabels[int(k[1])]=int(k[0])
	#print(trainlabels[int(k[1])])
	l=f.readline()
	n[int(k[0])]+=1

#initialize w
w=[]
for j in range(0, cols, 1):
    w.append(0)
    
for i in range(0, cols, 1):
    w[j] = w[j] + 0.2*random.random()- 0.1
	
#gradient descent iteration
eta=0.001

dellf = []
for j in range(0, cols, 1):
    dellf.append(0)
for i in range(0, rows, 1):
    dp = 0
    if(trainlabels.get(i) != None):
        dp=dot_product(w, data[i])
        for j in range(0, cols, 1):
            dellf[j] = dellf[j] + (trainlabels.get(i) -dp)*(data[i][j])

# update
for j in range(0,cols,1):
    w[j]=w[j]-eta*dellf[j]
    
#compute error
error = 0.0
for i in range(0,rows,1):
    if(trainlabels.get(i)!=None):
        error += float((-trainlabels.get(i) + dot_product(w, data[i]))**2)
print("error is:",error)
print("w=",w)
normw=0
for j in range(0,cols-1,1):
    normw+=w[j]**2
    print(w[j])
normw=math.sqrt(normw)
print("||w||=",normw)
# d_origin=w[w-1]/normw
# print("distance to origin=",d_origin)

#prediction
p={}
for i in range(0,rows,1):
	if(trainlabels.get(i)==None):
		dp=dot_product(w,data[i])
		if(dp>0):
			print("1",i)
			p[i]=1
		else:
			print("0",i)
			p[i]=0





    

