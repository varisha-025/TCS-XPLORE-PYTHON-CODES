pList=[]
class Player:
  def __init__(self,name,country,age,cFrom):
    self.name=name
    self.country=country
    self.age=age
    self.cFrom=cFrom
def count(pList,c_given):
  c=0
  for i in pList:
    if i.cFrom.lower()==c_given.lower():
      c+=1
  return c
def cmax(pList):
  max=len(pList[0].country)
  o=pList[0]
  for i in pList:
    if len(i.country)>max:
      max=len(i.country)
      o=i
  return o.name
if __name__=="__main__":
  t=int(input())
  for k in range(t):
    name=input()
    n=int(input())
    country=[]
    for i in range(n):
      country.append(input())
    age=int(input())
    cFrom=input()
    pList.append(Player(name,country,age,cFrom))
  c_given=input()
  print(count(pList,c_given))
  print(cmax(pList))