import os 
import numpy as np
import collections 

def scan(s,v):
    symb=""
    for ch in s:
        if((ch!='+')&(ch!="/")&(ch!=s[-1])): symb+=ch
        elif((symb=="")&(ch==s[-1])): v.append(ch)
        elif(symb!=""): v.append(symb); symb="" 

def printf(v):
    print("\n")
    count=0
    for i in range(len(v)//2):
        if(v[i]!=v[-1]): print(v[count]+"/"+v[count+1], end=''); count+=2
        if(i!=(len(v)//2)-1): print("+", end='')
    print()

def Calculate(x,y):
    arrnonzero = []
    summs = []
    sums_value = []
    value= []
    minimum_value = []
    max_value = []
    for i in range(len(x)//2):
        summs.append(np.add(x[i+i+1],y[1::2]))
        value = np.hstack((value,summs[i]))
        sums_value.append(np.fmin(x[i+i],y[0::2]))
        minimum_value = np.hstack((minimum_value, sums_value[i]))
    ends_value = np.vstack((value,minimum_value))
    counter = collections.Counter(value).most_common()
    counter1 = list(counter)
    counter1 = list(map(list,counter1))
    for i in range(len(counter1)):
        counter2 = list(map(str,counter1[i]))
        coun = int(counter2[1])
        if (coun >1) : 
            arrnonzero.append(counter2[0])
    if len(arrnonzero)!=0:
        for i in range(len(arrnonzero)):
            index = np.where(ends_value[0,]==float(arrnonzero[i]))
            max_value = float(0.0)
            for i in range(len(index[0])):
                max_value = np.maximum(ends_value[1][index[0][i]],max_value)
            index_delete = np.where(ends_value[1,]!=max_value)
            index1 = list(set(index[0]) & set(index_delete[0]))
            for i in range(len(set(index1).symmetric_difference(set(index[0])))-1):
                index1.append(index[0][i])
            ends_value = np.delete(ends_value , index1 , axis=1)
        ends_value[0] , ends_value[1] = list(ends_value[1]) , list(ends_value[0])
        ends_value = np.reshape(ends_value,len(ends_value)*len(ends_value[0]), order="f")
        return ends_value

def main():
    A=[]
    B=[]
    C = []
    print("Введите A")
    string="0.2/2+0.3/1+0.6/3+0.2/4"
    scan(string, A)
    printf(A)
    print("Введите B")
    string="0.1/5+1/1+0.5/2+0.6/4"
    scan(string, B)
    printf(B)
    A = list(map(float,A))
    B = list(map(float,B))
    C = Calculate(A,B)
    C = list(map(str,C))
    printf(C)

if __name__ == '__main__':
   main()