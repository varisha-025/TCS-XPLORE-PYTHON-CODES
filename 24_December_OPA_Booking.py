
class Booking:
  def __init__(self,id,no,date,guests,stat):
    self.id=id
    self.no=no
    self.date=date
    self.guests=guests
    self.stat=stat
  def table(self,d):
    if self.date==d and self.stat=="Reserved" or self.stat=="Booked":
      return self.no
    return -1
  def updatestat(self,d):
    if int(d[:2])-int(self.date[:2])>=2 and self.stat=="Reseved":
        self.stat="Cancelled"
    elif int(d[:2])-int(self.date[:2])>=1 and self.stat=="Booked":
        self.stat="Closed"
class Restaurant:
  def __init__(self,tlist,blist):
    self.tlist=tlist
    self.blist=[]
  def book(self,dg,ng,sg):
    tables=self.tlist
    b=[]
    idi=1
    for i in self.blist:
      b.append(i.table(dg))
    for i,j in tables.items():
        if i not in b and j==ng:
          self.blist.append(Booking(idi,i,dg,ng,sg))
          idi+=1
  def update(self,d):
    for i in self.blist:
      i.updatestat(d)
t=int(input())
tlist={}
for i in range(t):
  no=int(input())
  guests=int(input())
  tlist[no]=guests
blist=[]
ob=Restaurant(tlist,blist)
n=int(input())
date=input()
for i in range(n):
  guests=int(input())
  stat=input()
  if stat.lower()=="reserve":
    stat="Reserved"
  elif stat.lower()=="book":
    stat="Booked"
  ob.book(date,guests,stat)
d=input()
for i in blist:
  print(i.id,i.no,i.stat)
ng=int(input())
sg=input()
ob.update(d)
ob.book(d,ng,sg)
for i in blist:
  print(i.id,i.no,i.stat)