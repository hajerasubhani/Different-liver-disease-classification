import sys,os,re
import random

content_array=[]
traindata=[]
validdata=[]
dataset=input("enter your file name  ")
fp=open(dataset,"r")

for ln in fp:
    ln=ln.rstrip()
    ln=ln.lstrip()
    content_array.append(ln)

n=len(content_array)
out1=open("train.csv","w")
out2=open("validate.csv","w")
trno=int(n*0.8)
vno=n-trno
i=1
while i<=trno:
    j=random.randint(0,n-1)
    ln1=content_array[j]
    if ln1 in traindata:
        pass
    else:
        traindata.append(ln1)
        i=i+1
for l in traindata:
    out1.write(l)
    out1.write("\n")

for l in content_array:
    if l in traindata:
        pass
    else:
        out2.write(l)
        out2.write("\n")
fp.close()
out1.close
out2.close
