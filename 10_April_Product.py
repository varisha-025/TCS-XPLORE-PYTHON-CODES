class Product:
  def __init__(self,name,ptype,price,quan,requan):
    self.name=name
    self.ptype=ptype
    self.price=price
    self.quan=quan
    self.requan=requan
def find(plist,nlist):
  d={}
  for j in nlist:
    for i in plist:
      if j.lower()==i.name.lower():
        d[j]=i.quan
  if len(d)==0:
    return None
  else:
    return d
def update(plist,ng,ptypeg):
  flag=0
  for i in plist:
    if i.ptype.lower()==ptypeg.lower():
      if i.quan<=i.requan:
        flag=1
        i.quan+=ng
  if flag==0:
    return None
  else:
    return plist
if __name__=="__main__":
  plist=[]
  for i in range(5):
    name=input()
    ptype=input()
    price=int(input())
    quan=int(input())
    requan=int(input())
    plist.append(Product(name,ptype,price,quan,requan))
  n=int(input())
  nlist=[]
  for i in range(n):
    nlist.append(input())
  ng=int(input())
  ptypeg=input()
  v=find(plist,nlist)
  if v==None:
    print('Product Not Found.')
  else:
    for i in v:
      print(i,v[i])
  b=update(plist,ng,ptypeg)
  if b==None:
    print('Product Not Found.')
  else:
    for i in b:
      print(i.name,i.quan)