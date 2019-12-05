import numpy as np

class Shop(object):
    def __init__(self, name,number_people, max_long , longin, counter_turn):
        self.counter_turn = counter_turn
        self.name = name
        self.number_people = number_people
        self.max_long = max_long
        self.longin = longin

    def input(self,number_people, max_long):
        self.number_people = number_people
        if self.longin > self.max_long:
            print("people out from serv",self.number_people)
            return self.number_people, 0 
        else:
            self.longin += 1
            print(self.number_people," people come into shop, long of turn",self.longin) 
            return self.number_people, 1

    def serv(self,counter_turn):
        self.longin += self.counter_turn
        return "people go into to serv %s" %self.longin

    def exit(self):
        self.longin -= 1
        print("people exit with buy :)")
        return 


class Person(object):
    
    def __init__(self,number, max_turn):
        self.number = number
        self.max_turn = max_turn
    def input(self):
        print('person # ',self.number, 'go to shop')
        return  self.number,self.max_turn


class Turn(object):

    def __init__(self, lenght):
        self.lenght = lenght
        
    def long_turn(self, long_rutn ):
        return long_rutn

def main():
    palatka = Shop("palatka",1,3,0,0)
    for i in range(30):
        print("")
        person = Person(i,3)
        number_person, max_turn = person.input()
        a, flag_turn = palatka.input(number_person,max_turn)
        if flag_turn !=1:
            print("person go to home")
            
        else:
            print(palatka.serv(1))
        if np.random.randint(0,2) == 1 :
            palatka.exit()

if __name__ == '__main__':
   main()