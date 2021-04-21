class Movie:
  def __init__(self,id,name,price,cat):
    self.id=id
    self.name=name
    self.price=price
    self.cat=cat
  def category(self):
    if self.price>0 and self.price<150:
      self.cat="General"
    elif self.price>=150 and self.price<250:
      self.cat="Silver"
    elif self.price>=250 and self.price<350:
      self.cat="Gold"
    elif self.price>=350:
      self.cat="Platinum"
class Ticket:
  def __init__(self,cname,mname,vcount,total):
    self.cname=cname
    self.mname=mname
    self.vcount=vcount
    self.total=total
def getCount(mlist):
  d={"General":0,"Silver":0,"Gold":0,"Platinum":0}
  for i in mlist:
    if i.cat in d:
      d[i.cat]+=1
  return d
def book(mlist,cname,mgiven,vcount):
  flag=0
  for i in mlist:
    if i.name.lower()==mgiven.lower():
      flag=1
      t=i.price
  if flag==0:
    return None
  else:
    return Ticket(cname,mname,vcount,t*vcount)
if __name__=="__main__":
  t=int(input())
  mlist=[]
  for i in range(t):
    id=int(input())
    name=input()
    price=int(input())
    ob=Movie(id,name,price,"Default")
    ob.category()
    mlist.append(ob)
  v=getCount(mlist)
  print("Category wise ticket count:")
  for i in v:
      if v[i]!=0:
        print(i+':'+str(v[i]))
  cname=input()
  mname=input()
  vcount=int(input())
  b=book(mlist,cname,mname,vcount)
  if b==None:
    print('Movie not available')
  else:
    print(b.cname,b.total)