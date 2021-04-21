table=[]
class Table:
  def __init__(self,num,name,stat):
    self.num=num
    self.name=name
    self.stat=stat
def total(table):
  p=[]
  nam=[]
  for k in table:
      nam.append(k.name)
  for i in table:
      c=0
      for j in range(len(nam)):
        if i.name.strip() in nam[j].strip():
          c+=1
      p.append([i.name,c])
  p=dict(p)
  return p
def find(table,ng):
  for i in table:
    if i.num==ng:
      return i.name
  return None
if __name__=="__main__":
  t=int(input())
  for i in range(t):
    num=int(input())
    name=input()
    stat=input()
    table.append(Table(num,name,stat))
  ng=int(input())
  f=total(table)
  for k in sorted(f.keys()):
      print(k+'-'+str(f[k]))
  s=find(table,ng)
  if s==None:
      print('No table found')
  else:
      print(s)