class Player:
  def __init__(self,name,country,age,matches,runs,wickets):
    self.name=name
    self.country=country
    self.age=age
    self.matches=matches
    self.runs=runs
    self.wickets=wickets
class Team:
  def __init__(self,playerlist):
    self.playerlist=playerlist
  def minRuns(self):
    min=self.playerlist[0]
    for i in self.playerlist:
      if i.runs<min:
        min=i.runs
        ob=i
    return ob
  def maxWickets(self):
    max=self.playerlist[0]
    for i in self.playerlist:
      if i.wickets>max:
        max=i.wickets
        ob=i
    return ob
if __name__=="__main__":
  n=int(input())
  playerlist=[]
  for i in range(n):
    name=input()
    country=input()
    age=int(input())
    runs=int(input())
    wickets=int(input())
    playerlist.append(Player(name,country,age,runs,wickets))
  ob=Team(playerlist)
  o1=ob.minRuns()
  print(o1.name)
  print(o1.runs)
  print(o1.country)
  o2=ob.maxWickets()
  print(o2.name)
  print(o2.wickets)
  print(o2.country)
