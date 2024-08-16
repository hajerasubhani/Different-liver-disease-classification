import re
import sys
import os
import codecs

inf=codecs.open("SVMop.txt",'r',encoding='utf-8')
tcnt=0
tp=0
fp=0
gg=0
gb=0
bb=0
bg=0

for ln in inf:
    tcnt=tcnt+1
    ln=ln.rstrip()
    ln=ln.lstrip()
    tks=ln.split(",")
    acls=tks[0]
    pcls=tks[1]
    acls=acls.lstrip()
    acls=acls.rstrip()
    pcls=pcls.lstrip()
    pcls=pcls.rstrip()
    print(acls ,pcls)
    #acls=acls.lower()  # converting into lower case
    #pcls=pcls.lower()
    acls=int(acls)
    pcls=int(pcls)
    
    if acls==1:
        if acls==pcls:
            gg=gg+1
            tp=tp+1
           # print(tp)
        else:
            gb=gb+1
            #print(gb)
            fp=fp+1
    else:
        if acls==pcls:
            bb=bb+1
            tp=tp+1
            #print(tp)
           # print(bb)
            #tn=tn+1
        else:
            bg=bg+1
            fp=fp+1

print("1 as 1",gg,"\n")
print("1 as 2",gb,"\n")
print("2 as 2",bb,"\n")
print("1 as 1",bg,"\n")

          
            
#gprecision=float(gg)/(gg+bg)  #tp/tp+fp
#bprecision=float(bb)/(bb+gb)

#grecall=float(gg)/(gg+gb)       #tp/tp+fn
#brecall=float(bb)/(bb+bg)

#print("no. of good precision=",gprecision)
#print("no. of bad precision=",bprecision)

#print("no. of good recall=",grecall)
#print("no. of bad recall=",brecall)
precision=precision=float(tp)/(tp+fp)
recall=float(tp)/(tp+fn)

precision=float(gg)/(gg+bg)
recall=float(gg)/(gg+gb)
fmeasure=float(2*precision*recall)/(precision+recall)

accuracy=float(gg+bb)/(gg+bb+gb+bg)  ##accuracy=(tp+tn)/(tp+tn+fp+fn)

error=1-accuracy

sensitivity=float(tp)/(tp+fn)

##specificity=float(tn)/(tn+fp)
specificity=float(tn)/(tn+fp)
print("precision=",precision,"\n")
print("recall=",recall,"\n")
print("fmeasure=",fmeasure,"\n")
print("sensitivity=",sensitivity,"\n")
print("specificity=",specificity,"\n")




print("no. of cases correctly recognize=",tp,accuracy)
print(" no. of cases wrongly recognize=",fp,error)

     
