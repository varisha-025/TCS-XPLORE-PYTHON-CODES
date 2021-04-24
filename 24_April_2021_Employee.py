class Employee:
  def __init__(self,id,name,dep,sal,role):
    self.id=id
    self.name=name
    self.dep=dep
    self.sal=sal
    self.role=role
  def calc_incentive(self,dg):
      for i,j in dg.items():
          if i.lower().strip()==self.role.lower().strip():
              inc=(self.sal*dg[i])/100
              self.sal+=inc
              return inc
      return None
def calc(rg,el,dg):
    m=[]
    f=0
    for i in el:
        if f!=0:
            if i.role.lower().strip()==rg.lower().strip():
                p=i.calc_incentive(dg)
                m.append(i)
        f+=1
    return m

if __name__=="__main__":
  t=int(input())
  d={}
  for i in range(t):
    role=input()
    ip=int(input())
    d[role]=ip
  el=[]
  n=int(input())
  for i in range(n):
    id=int(input())
    name=input()
    dep=input()
    sal=int(input())
    role=input()
    if i!=0:
        el.append(Employee(id,name,dep,sal,role))
    else:
        v=Employee(id,name,dep,sal,role)
        el.append(v)
  rg=input()
  p=v.calc_incentive(d)
  if p==None:
    print('Employee Not Found.')
  else:
      print(p)
  if v.role.lower().strip()==rg.lower().strip():
      print(v.id,v.name,v.sal)
  q=calc(rg,el,d)
  if len(q)!=0:
      for i in q:
        print(i.id,i.name,i.sal)
  else:
    print('Employee Not Found.')
