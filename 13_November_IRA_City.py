
class City:
  def __init__(self,id,sname,cname,tests,pos):
    self.id=id
    self.sname=sname
    self.cname=cname
    self.tests=tests
    self.pos=pos
class Analysis:
  def __init__(self,aname,clist):
    self.aname=aname
    self.clist=clist
  def get1(self):
    v=[]
    m,sn=" "," "
    max=0
    for i in self.clist:
      v.append(i.sname)
    for j in v:
      c=0
      for i in self.clist:
        if i.sname==j:
          c+=i.pos
          m=i.sname
      if c>max:
        max=c
        sn=m
    return sn
  def get2(self,pgiven):
    b=[]
    flag=0
    for i in self.clist:
      p=(i.pos*100)/i.tests
      if p>=pgiven:
        flag=1
        b.append([i.sname,i.cname])
    if flag==0:
      return None
    else:
      return b
if __name__=="__main__":
  t=int(input())
  clist=[]
  for i in range(t):
    id=int(input())
    sname=input()
    cname=input()
    tests=int(input())
    pos=int(input())
    clist.append(City(id,sname,cname,tests,pos))
  pgiven=int(input())
  ob=Analysis("abc",clist)
  print(ob.get1())
  d=ob.get2(pgiven)
  if d==None:
    print('No city recorded with the given percentage.')
  else:
    for j,h in d:
      print(j,h)