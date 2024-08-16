import sys,os,re

tksdict={}
infname=input("enter your file name  ")
fp=open(infname,"r")
i=1
for ln in fp:
    ln=ln.rstrip()
    ln=ln.lstrip()
    if i==1:
        pass
    else:
        tks=ln.split(",")
        tk=tks[2]
        tksdict[tk]=tksdict.get(tk,0)+1
    i=i+1
print("number rows",i)
print("number of unique values is ",len(tksdict))
for k in tksdict.keys():
    v=tksdict[k]
    print(k,"\t",v)
        
