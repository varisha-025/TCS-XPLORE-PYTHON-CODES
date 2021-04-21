class Product:
  def __init__(self,name,ptype,price,qnty):
    self.name=name
    self.ptype=ptype
    self.price=price
    self.qnty=qnty
class Store:
  def __init__(self,productList):
    self.productList=productList
  def purchase(self,n_given,qnty_given):
    bill=0
    for i in self.productList:
      if i.name.lower()==n_given.lower():
        if i.qnty==0:
          return None
        elif qnty_given>i.qnty:
          bill=i.price*i.qnty
          i.qnty-=i.qnty
          return bill
        elif qnty_given<=i.qnty:
          bill=i.price*qnty_given
          i.qnty=i.qnty-qnty_given
          return bill
    return None
if __name__=='__main__':
  n=int(input())
  productList=[]
  for i in range(n):
    name=input()
    ptype=input()
    price=int(input())
    qnty=int(input())
    productList.append(Product(name,ptype,price,qnty))
  ob=Store(productList)
  n_given=input()
  qnty_given=int(input())
  p=ob.purchase(n_given,qnty_given)
  if p==None:
      print('Product not available.')
  else:
      print(p)
  for i in productList:
    print(i.name,i.qnty)
