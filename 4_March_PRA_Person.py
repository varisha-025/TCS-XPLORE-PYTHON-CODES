
class Person:
  def __init__(self,name,h,w):
    self.name=name
    self.h=h
    self.w=w
class Society:
  def __init__(self,personList):
    self.personList=personList
  def avg(self):
    s=0
    for i in self.personList:
      s+=i.h
    return s/len(personList)
  def find(self,av):
    p=[]
    for i in self.personList:
      if i.h>av:
        p.append(i.name)
    return p
if __name__=='__main__':
  n=int(input())
  personList=[]
  for i in range(n):
    name=input()
    h=int(input())
    w=int(input())
    personList.append(Person(name,h,w))
  ob=Society(personList)
  av=ob.avg()
  print('The average height is:',av)
  y=ob.find(av)
  print('Persons taller than average height')
  for i in y:
    print(i)