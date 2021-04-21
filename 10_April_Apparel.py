class Apparel:
  def __init__(self,brand,ptype,price,avail):
    self.brand=brand
    self.ptype=ptype
    self.price=price
    self.avail=avail
class Store:
  def __init__(self,alist):
    self.alist=alist
  def check(self,brandg,typeg,sizeg,quan):
    for i in self.alist:
      if i.brand==brandg and i.ptype==typeg:
          flag=1
          for j,k in i.avail.items():
            if j==sizeg and k>=quan:
              i.avail[sizeg]-=quan
              return True
    return False
if __name__=="__main__":
  t=int(input())
  alist=[]
  for i in range(t):
    brand=input()
    ptype=input()
    price=int(input())
    n=int(input())
    avail={}
    for k in range(n):
      size=input().upper()
      quantity=int(input())
      avail[size]=quantity
    alist.append(Apparel(brand,ptype,price,avail))
  ob=Store(alist)
  bg=input()
  tg=input()
  sg=input()
  qg=int(input())
  v=ob.check(bg,tg,sg,qg)
  if v==True:
    print('Size is Available')
  else:
    print('Size is not available')
  flag=0
  for i in alist:
    if i.brand==bg and i.ptype==tg:
      flag=1
      for k in i.avail:
          print(k,":",str(i.avail[k]))
  if flag==0:
    print('Apparel not found')