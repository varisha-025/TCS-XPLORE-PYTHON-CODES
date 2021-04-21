
goldList=[]
class GoldInvoice:
  def __init__(self,id,name,quantity,rate,weight,pwc,pdis):
    self.id=id
    self.name=name
    self.quantity=quantity
    self.rate=rate
    self.weight=weight
    self.pwc=pwc
    self.pdis=pdis
  def calcExGST(self,goldList,id_choice):
    for i in goldList:
      if i.id==id_choice:
        cost=i.rate*i.quantity*i.weight
        pw=i.pwc*cost/100
        pd=i.pdis*cost/100
        return cost+pw-pd
  def calcInGST(self,goldList,id_choice):
    for i in goldList:
      if i.id==id_choice:
        cost=i.rate*i.quantity*i.weight
        pw=i.pwc*cost/100
        pd=i.pdis*cost/100
        gst=0.03*cost
        return cost+pw-pd+gst
if __name__=='__main__':
    n=int(input())
    for i in range(n):
      id=int(input())
      name=input()
      qnty=float(input())
      rate=float(input())
      weight=float(input())
      pwc=float(input())
      pdis=float(input())
      goldList.append(GoldInvoice(id,name,qnty,rate,weight,pwc,pdis))
    ob=GoldInvoice(0,'',0,0,0,0,0)
    id_choice=int(input())
    p=ob.calcExGST(goldList,id_choice)
    print('%.3f'%p)
    g=ob.calcInGST(goldList,id_choice)
    print('%.2f'%g)