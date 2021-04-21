class Product:
  def __init__(self,id,name,ptype,price):
    self.id=id
    self.name=name
    self.ptype=ptype
    self.price=price
  def discount(self,dis):
      self.price-=(self.price*dis)/100
class Store:
  def __init__(self,sname,plist):
    self.sname=sname
    self.plist=plist
  def calc(self,dis,p):
    b={}
    flag=0
    for i in self.plist:
      if i.ptype.lower()==p.lower():
        flag=1
        i.discount(dis)
        b[i.price]=i.name
    if flag==1:
      return b
    else:
      return None
t=int(input())
plist=[]
for i in range(t):
  id=int(input())
  name=input()
  ptype=input()
  price=int(input())
  plist.append(Product(id,name,ptype,price))
ob=Store("abc",plist)
p=input()
d=int(input())
s=ob.calc(d,p)
if s==None:
  print('Product not found')
else:
    for i in sorted(s,reverse=True):
      print(s[i],i)