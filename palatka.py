from queue import Queue
from threading import Thread
import time
import random

class Customer(object):
 
    def __init__(self, number):
        """Constructor"""
        self.number = number
    
    def come(self):
        return "Человек № %s решил заглянуть в палатку" % self.number 
    
    def leave(self):
        return "Человек ушел" 

    def order(self,q):
        if((not(q.empty()))&(q.qsize()<3)):q.put(self); print("Человек",self.number,"встает в очередь, размер очереди:", q.qsize())
        elif(q.qsize()>=3): print("Человек", self.number, "не хочет стоять в очереди, размер очереди:", q.qsize())
        elif(q.empty()): q.put(self); print("Человек",self.number,"подходит к палатке чтобы сделать заказ")
        return self.number
    
class Cashier(object):

    def __init__(self, q):
        self.q=q

    def service(self):
        print("Кассир начинает обслуживать покупателя")

    def servcomplete(self):
        amount = random.randint(4, 7)
        time.sleep(amount)
        self.cu=(self.q.get()).number
        self.cust=Customer(self.cu)
        print("Кассир завершил обслуживание покупателя ", self.cu)


def serv(qc, cash):
    if(qc.empty()): time.sleep(1.2)
    while(not(qc.empty())):
        if(not(qc.empty())): cash.service(); cash.servcomplete()

def people(qc,lenght):
    for i in range(1,lenght+1):
        cust=Customer(i)
        print(cust.come())
        cust.order(qc)
        amount = random.randint(2, 3)
        time.sleep(amount)
    
def main():
    q=Queue()
    cash=Cashier(q)
    lenght=30 #длина очереди
    thr1=Thread(target=serv, args=(q,cash))
    thr2=Thread(target=people, args=(q,lenght))
    thr1.start() 
    thr2.start()
    thr1.join()
    thr2.join() 

if __name__== '__main__':
   main()