class Blood:
  def __init__(self,group,unit):
    self.group=group
    self.unit=unit
class BloodBank:
  def __init__(self,bloodList):
    self.bloodList=bloodList
  def available(self,group_given,unit_given):
    for i in self.bloodList:
      if i.group.upper()==group_given.upper() and i.unit>=unit_given:
        return True
    return False
  def minBlood(self):
    min=self.bloodList[0].unit
    l=[]
    for i in self.bloodList:
      if i.unit<min:
        min=i.unit
    for i in self.bloodList:
      if i.unit==min:
        l.append(i.group)
    return l
if __name__=='__main__':
  n=int(input())
  bloodList=[]
  for i in range(n):
    grp=input().upper()
    unit=int(input())
    bloodList.append(Blood(grp,unit))
  ob=BloodBank(bloodList)
  group_given=input()
  unit_given=int(input())
  p=ob.available(group_given,unit_given)
  if p==True:
    print('Blood Available')
  else:
    print('Blood Not Available')
  j=ob.minBlood()
  for i in j:
    print(i)