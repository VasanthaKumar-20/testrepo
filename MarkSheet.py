n=str(input("\n NAME: \t"))
print("\n ---------------------------------------------\t")
r=int(input("\n Reg.No.:\t"))
print("\n ---------------------------------------------\t")
t=int(input("\n TAMIL : \t"))
print("\n ---------------------------------------------\t")
e=int(input("\n ENGLISH : \t"))
print("\n ---------------------------------------------\t")
m=int(input("\n MATHS: \t"))
print("\n ---------------------------------------------\t")
p=int(input("\n PHYSICS: \t"))
print("\n ---------------------------------------------\t")
c=int(input("\n CHEMISTRY: \t"))
print("\n ---------------------------------------------\t")
cs=int(input("\n CS/BIO: \t"))
print("\n ---------------------------------------------\t")
tot=t+e+m+p+c+cs
co=(m+(p+c)/2)
print("\n TOTAL: \t",tot)
print("\n ---------------------------------------------\t")
print("\n CutOff: \t",co)
if(co>=177.5):
    print("\n GradeA \t")
elif(co<177.5 and co>=155.5):
    print("\n Grade B \t")
elif(co<155.5 and co>=135.5):
    print("\n Grade C \t")
elif(co<135.5 and co>=115.5):
    print("\n Grade D \t")
else:
    print("\n Grade E \t")
