
class Container:
  def __init__(self,id,length,breadth,heigth,priceSqrFt):
    self.id=id
    self.length=length
    self.breadth=breadth
    self.heigth=heigth
    self.priceSqrFt=priceSqrFt
  def findVolume(self):
    return self.length*self.breadth*self.heigth
class PackagingCompany:
  def __init__(self,conList):
    self.conList=conList
  def cost(self,id_given):
    for i in self.conList:
      if i.id==id_given:
        return i.findVolume()*i.priceSqrFt
      else:
        return None
  def largest(self):
    maxV=0
    l,c=[],[]
    for i in self.conList:
      l.append(i.findVolume())
      c.append(i)
    f=zip(c,l)
    l.sort()
    for i in f:
      if i[1]==l[-2]:
        return i[0]
if __name__=='__main__':
  n=int(input())
  conList=[]
  for i in range(n):
    id=int(input())
    l=int(input())
    b=int(input())
    heigth=int(input())
    price=int(input())
    conList.append(Container(id,l,b,heigth,price))
  p=PackagingCompany(conList)
  id_given=int(input())
  if p.cost(id_given)==None:
    print('No container found')
  else:
    print(p.cost(id_given))
  ob=p.largest()
  print(ob.id,ob.findVolume())