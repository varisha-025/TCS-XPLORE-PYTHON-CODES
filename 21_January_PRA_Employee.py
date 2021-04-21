
class Employee:
  def __init__(self,id,name,status,age):
    self.id=id
    self.name=name
    self.status=status
    self.age=age
class Organisation:
  def __init__(self,employeeList):
    self.employeeList=employeeList
  def update(self,years):
    for i in self.employeeList:
      if i.age>years:
        i.status='Retirement Due'
  def count(self):
    c=0
    for i in self.employeeList:
      if i.status=='Retirement Due':
        c+=1
    return c
if __name__=='__main__':
  n=int(input())
  employeeList=[]
  for i in range(n):
    id=int(input())
    name=input()
    age=int(input())
    employeeList.append(Employee(id,name,'In Service',age))
  years=int(input())
  ob=Organisation(employeeList)
  ob.update(years)
  g=ob.count()
  if g==0:
    print('No Employees Updated')
  else:
    print('Count of employee updated=',g)
  for i in employeeList:
    print(i.id,i.name,i.status)