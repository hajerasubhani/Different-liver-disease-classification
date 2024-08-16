import sys,os,re
import random
content_array=[]
tr1=[]
indx=0

out1=open("tr1.csv","w")
out2=open("tr2.csv","w")
out3=open("tr3.csv","w")
out4=open("tr4.csv","w")
out5=open("tr5.csv","w")
out6=open("tr6.csv","w")
out7=open("tr7.csv","w")
out8=open("tr8.csv","w")
out9=open("tr9.csv","w")
out10=open("tr10.csv","w")

dataset=input("enter your file name  ")
fp=open(dataset,"r")

for ln in fp:
    ln=ln.rstrip()
    ln=ln.lstrip()
    content_array.append(ln)

n=len(content_array)


trno=int(n/10)
print(trno)

for i in range(0,n):
    indx=random.randint(0,n-1)
    
    if i<=57:
        ln=content_array[indx]
        print(i,indx,ln)
        ln=str(ln)
        
        out1.write(ln)
        out1.write("\n")
    elif i>57 and i<=115:
        ln=content_array[indx]
        out2.write(ln)
        out2.write("\n")
    elif i>115 and i<=173:
        ln=content_array[indx]
        out3.write(ln)
        out3.write("\n")
    elif i>173 and i<=231:
        ln=content_array[indx]
        out4.write(ln)
        out4.write("\n")
    elif i>231 and i<=289:
        ln=content_array[indx]
        out5.write(ln)
        out5.write("\n")
    elif i>289 and i<=347:
        ln=content_array[indx]
        out6.write(ln)
        out6.write("\n")
    elif i>347 and i<=405:
        ln=content_array[indx]
        out7.write(ln)
        out7.write("\n")
    elif i>405 and i<=463:
        ln=content_array[indx]
        out8.write(ln)
        out8.write("\n")
    elif i>463 and i<=521:
        ln=content_array[indx]
        out9.write(ln)
        out9.write("\n")
    else:
        ln=content_array[indx]
        out10.write(ln)
        out10.write("\n")


fp.close()
out1.close()
out2.close()
out3.close()
out4.close()
out5.close()
out6.close()
out7.close()
out8.close()
out9.close()
out10.close()

