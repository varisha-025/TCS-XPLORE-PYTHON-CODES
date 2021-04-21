class Item:
  def __init__(self,name,ptype,price):
    self.name=name
    self.ptype=ptype
    self.price=price
class Store:
  def __init__(self,productList):
    self.productList=productList
  def purchase(self,n_given,qnty_given):
    bill=0
    for i,qnty in productList.items():
          if i.name.lower().strip()==n_given.lower().strip():
            if qnty==0:
                return None
            elif qnty_given>qnty:
                bill=i.price*qnty
                productList[i]=0
                return bill
            elif qnty_given<=qnty:
                bill=i.price*qnty_given
                productList[i]=productList[i]-qnty_given
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
    ob1=Item(name,ptype,price)
    productList.append([ob1,qnty])
  productList=dict(productList)
  ob2=Store(productList)
  num=int(input())
  order=[]
  for k in range(num):
    n_given=input()
    qnty_given=int(input())
    order.append([n_given,qnty_given])
  order=dict(order)
  for k,q in order.items():
    s=ob2.purchase(k,q)
    if s==None:
        print(k.lower().strip(),'is not available')
    else:
        print('Bill of the item',k.lower().strip(),'=',s)
  print('Stock in Hand:')
  for i in productList:
      print(i.name.strip(),productList[i])