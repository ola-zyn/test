f=open("slowa.txt", "r")
a=open("slowa_a.txt", "w")
b=open("hasla_a.txt", "w")
c=open("hasla_b.txt", "w")
d=open("slowa_b.txt", "w")


def czyPalindrom(a):
    T=list(a)
    T2=list(a)
    T2.reverse()
    if(T==T2):
        return True
    return False


def koncowka(s):
    x1=""
    x2=""
    T=[]
    T2=[]
    for i in range(len(s)):
        x1=x1+s[i]
        if(czyPalindrom(x1)):
            x2=""
        else:
            x2=s[i]+x2
    return x2







T=[]
Tod=[]
X=[]
i=0
max=0
min=30
inmax=0
inmin=0
for linia in f:
    linia=linia.strip()
    T.append(linia)
    if(len(linia)>max):
        max=len(linia)
        inmax=i
    if (len(linia) < min):
        min = len(linia)
        inmin=i
    X=list(linia)
    X.reverse()
    linia="".join(X)
    Tod.append(linia)
    b.write(linia+"\n")
    i+=1


a.write(Tod[inmax]+" "+str(max)+"\n")
a.write(Tod[inmin]+" "+str(min))




max=0
min=100
inmax=0
inmin=0
s=0
d.write("1.\n")
for i in range(len(T)):
    c.write(koncowka(T[i])+T[i]+"\n")
    s+=len(koncowka(T[i]))+len(T[i])
    if(len(koncowka(T[i]))+len(T[i])==12):
        d.write(koncowka(T[i])+T[i]+"\n")
    if (len(koncowka(T[i])) + len(T[i]) > max):
        max=len(koncowka(T[i])) + len(T[i])
        inmax=i
    if (len(koncowka(T[i])) + len(T[i]) < min):
        min=len(koncowka(T[i])) + len(T[i])
        inmin=i

d.write("2.\n")
d.write(koncowka(T[inmax]) + T[inmax]+"\n")
d.write(koncowka(T[inmin]) + T[inmin]+"\n")
d.write("3.\n")
d.write(str(s))
f.close()
a.close()
b.close()
c.close()
d.close()