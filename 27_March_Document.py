class Document:
  def __init__(self,id,name,details):
    self.id=id
    self.name=name
    self.details=details
class Archive:
  def __init__(self,aid,dlist):
    self.aid=aid
    self.dlist=dlist
  def find(self):
    p=[]
    for i in self.dlist:
      for j in i.details:
          if "/" in j:
              l=(i.id,j)
              p.append(l)
    return p
  def count(self,sgiven):
    c=0
    for i in self.dlist:
      n,t=i.name.split('.')
      if t==sgiven:
        c+=1
    return c
if __name__=="__main__":
  t=int(input())
  dlist=[]
  for i in range(t):
    id=int(input())
    name=input()
    details=input().split(",")
    dlist.append(Document(id,name,details))
  ob=Archive("TCS",dlist)
  stype=input()
  d=ob.find()
  if len(d)!=0:
    for i in d:
      print(i[0],i[1].strip())
  p=ob.count(stype)
  print("Document Count =",p)