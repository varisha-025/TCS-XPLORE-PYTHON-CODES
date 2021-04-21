class Person:
  def __init__(self,name,h,w,bmi=0,status=""):
    self.name=name
    self.h=h
    self.w=w
    self.bmi=bmi
    self.status=status
  def calc1(self):
    self.bmi=round(self.w/(self.h*self.h))
class Society:
  def __init__(self,plist,bstat):
    self.plist=plist
    self.bstat=bstat
  def calc2(self,ng):
    for i in self.plist:
      if i.name.lower()==ng.lower():
        i.calc1()
        for j,k in self.bstat.items():
          if k[0]<i.bmi<k[1]:
            i.status=j
            return True
    return False
  def remove(self,bg):
    b=[]
    for i in self.plist:
      if i.bmi<bg:
        b.append(i)
    return b
t=int(input())
plist=[]
for i in range(t):
  name=input()
  h=int(input())
  w=int(input())
  plist.append(Person(name,h,w,0,""))
n=int(input())
bstat={}
for i in range(n):
  bs=input()
  lb=int(input())
  ub=int(input())
  if lb>ub:
    lb,ub=ub,lb
  bstat[bs]=(lb,ub)
ob=Society(plist,bstat)
ng=input()
p=ob.calc2(ng)
if p==True:
  for i in plist:
    if i.bmi!=0 or i.name.lower()==ng.lower():
      print(i.bmi,i.status)
else:
  print("No Person Exists")
bg=int(input())
v=ob.remove(bg)
for k in v:
  print(k.name,k.bmi)