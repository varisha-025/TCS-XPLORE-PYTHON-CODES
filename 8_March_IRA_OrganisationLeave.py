
class OrganisationLeave:
  def __init__(self,name,des,salary,balance):
    self.name=name
    self.des=des
    self.salary=salary
    self.balance=balance
class Organisation:
  def __init__(self,el):
    self.el=el
  def check(self,ng,leave,days):
    for i in self.el:
      if i.name.lower()==ng.lower():
        for l,c in i.balance.items():
          if l==leave and days<=c:
            i.balance[l]-=days
            return True
    return False
if __name__=="__main__":
  t=int(input())
  el=[]
  for i in range(t):
    name=input()
    des=input()
    salary=int(input())
    n=int(input())
    balance={}
    for j in range(n):
      lt=input().upper()
      nd=int(input())
      balance[lt]=nd
    el.append(OrganisationLeave(name,des,salary,balance))
  ng=input()
  leave=input().upper()
  days=int(input())
  ob=Organisation(el)
  s=ob.check(ng,leave,days)
  if s==True:
    print('Leave granted.')
  else:
    print('Leave not granted.')
  flag=0
  for i in el:
      if i.name.lower()==ng.lower():
        flag=1
        for j,h in i.balance.items():
          print(j+':'+str(h))
  if flag==0:
      print('Employee not found.')