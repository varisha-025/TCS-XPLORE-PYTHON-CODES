class News:
  def __init__(self,no,year,name,price):
    self.no=no
    self.year=year
    self.name=name
    self.price=price
class Agency:
  def __init__(self,db):
    self.db=db
  def search(self,yg):
    b=[]
    flag=0
    for i,j in self.db.items():
      if j.year==yg:
        flag=1
        b.append(j)
    if flag==1:
      return b
    else:
      return None
  def calc(self,ng):
    total=0
    for i,j in self.db.items():
      if j.name==ng:
        total+=j.price
    return total
if __name__=="__main__":
  t=int(input())
  db={}
  for i in range(t):
    no=input()
    year=int(input())
    name=input()
    price=int(input())
    db[no]=News(no,year,name,price)
  ob=Agency(db)
  yg=int(input())
  s=ob.search(yg)
  if s!=None:
    for i in s:
      print(i.no)
      print(i.name)
      print(i.year)
      print(i.price)
  else:
    print("No newspaper found")
  ng=input()
  v=ob.calc(ng)
  print("Total price:",v)