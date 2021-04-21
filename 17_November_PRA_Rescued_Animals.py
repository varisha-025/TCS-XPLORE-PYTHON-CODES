class RescuedAnimal:
  def __init__(self,id,cat,breed,status):
    self.id=id
    self.cat=cat
    self.breed=breed
    self.status=status
class AdoptionCenter:
  def __init__(self,cid,animalList):
    self.cid=cid
    self.animalList=animalList
  def count(self):
    cl,d=[],[]
    c=0
    for i in self.animalList:
      cl.append(i.cat)
    for j in cl:
      c=0
      for i in self.animalList:
        if i.cat==j:
          c+=1
      d.append([j,c])
    d=dict(d)
    return d
  def adopt(self,given):
    for i in self.animalList:
      if i.id==given:
        s= i.status
    if s=='Healthy':
      return 1
    elif s=='Unhealthy':
      return 2
    elif s=='Traumatied':
      return 3
    elif s=='Critical':
      return 4
if __name__=='__main__':
  n=int(input())
  animalList=[]
  for i in range(n):
    id=int(input())
    cat=input()
    breed=input()
    status=input()
    animalList.append(RescuedAnimal(id,cat,breed,status))
  given=int(input())
  ob=AdoptionCenter(given,animalList)
  t=ob.count()
  for i in t:
    print(i,t[i])
  p=ob.adopt(given)
  given=str(given)
  if p==1:
    print(given+':'+'Available for adoption')
  elif p==2:
    print(given+':'+'Undergoing Treatment')
  elif p==3:
    print(given+':'+'Undergoing Trauma Care')
  elif p==4:
    print(given+':'+'Unavailable for adoption')