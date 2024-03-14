import time
import random
import itertools
import copy
import math
from itertools import chain, combinations
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#                        algorithm moor and  
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
start_time = time.time()

def impo(filname):
    p=[]
    with open(filname) as f:
        for l in f :
            p.append([int(n) for n in l.strip().split('\t')])
            
    nb=p[0][0]
    data=[]
    for i in range(nb):
        data.append([i+1,int(p[1][i]),int(p[2][i])])
    return data 


def impo2(filname):
    p=[]
    with open(filname) as f:
        for l in f :
            p.append([int(n) for n in l.strip().split('\t')])
            
    nb=p[0][0]
    data=[]
    for i in range(nb):
        data.append([i+1,int(p[1][i]),int(p[2][i]),int(p[3][i]),int(p[4][i])])
    return data



def ord(t):#  ordonner les taches selant les dates d’échéance des tâches di
    t.sort(key=lambda  k:(k[2])) 
    return t


def fuun(y,e):
    mx=0
    for i in range(len(y)):
        for j in range(len(e)):
            if y[i]==e[j][0] and mx<e[j][1]: # ce bloc d'instruction permet    
                mx=e[j][1]                   # de determiner la tche dont la duree est superieur pour 
                ele_a_retire=e[j][0]         #la retirer dans la liste des tache sont retard
    y.remove(ele_a_retire)  # retirer  la tache 
    return y,mx,ele_a_retire # le mx pour   deduction de la dure de lache retir & ele_a_retire pour garder les elements retiree dans une list  


def fff(e):
    e=ord(e)
    somme_pi=0# somme des durie des tache qui ne sont pas en retard (les tache qui sont dans la liste t1)
    t1=[]# cette liste va contiet les taches qui ne sont pas en retard 
    t2=[]# cette liste va garder les tache retirer dans t1
    foct_obje=0
    for i in range(len(e)):
        t1.append(e[i][0])# 
        somme_pi+=e[i][1]# la dure de la tche que ona que o nait vient d'ajouter a list 
        if somme_pi>e[i][2]:# cd pour tester si la tache est en retard ou non? 
           t1,pi,tach_retirer=fuun(t1,e)# cette fonction va retirer la tche avecla dure sup parmi les taches de la list t1 
           somme_pi-=pi  # deduction de la dure de lache retir
           t2.append(tach_retirer)
           foct_obje+=1
    t1=t1+t2
    print('la fct objec=',foct_obje)
    return t1,foct_obje
    
print("--- %s seconds ---" % (time.time() - start_time))         

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#                        metaheyristique   
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#                       objectif 1:
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#



def swap(t):
  c=0
  a=0
  while c == a:
    c = random.randint(0,len(t)-1)
    a = random.randint(0,len(t)-1)
  t2=t[:]
  t2[c],t2[a] = t2[a],t2[c]
  return t2

def inse_op(t):
  c=0
  a=0
  while c == a:
    a=random.randint(0, len(t)-1)
    c=random.randint(0, len(t)-1)
  t2=t[:]
  f=t2.pop(a)
  t2.insert(c,f)
  return t2
def deux_opt(t):
  a=0
  b=0
  while(a==b and b-a<1 ):
    a=random.randint(0,len(t)//2)
    b=random.randint((len(t)+1)//2,len(t)-1)
  t1=t[:a]
  t2=t[b-1:]
  t3=t[a:b-1]
  t3.reverse()

  return t1+t3+t2

def val_obj_fun(seq):
    val=0
    c=0
    seqq=[]
    for i in range(len(seq)):
        c+=seq[i][1]
        seqq.append(seq[i][0])
        if c>seq[i][2]:
            val+=1
    return val




def N(x,k):  # cette fonction regroupe les stucture de voisinage qui va etre utilser dans le bloc de shaking (shakimg phss)  
    if k==1:
        return deux_opt(x)
    elif k==0:
        return inse_op(x)
    else:
        return swap(x)

def N1(x,l):  #  cette fonction regroupe les stucture de voisinage qui va etre utilser dans le bloc de (phse de) "local searsh  VND"  
    if l==0:
        return deux_opt(x)
    elif l==1:
        
        return inse_op(x)
    else:
        return swap(x)
start_time=time.time()

def Rvns(x):

    l=0
    while((time.time() - start_time)<20):
    
         c=0
         x2=N(x,l)
         a=val_obj_fun(x)
         b=val_obj_fun(x2)
         if b<=a:
            x=x2[:]
         c+=1
         if c>3:
            l+=1
         l+=1
  
    return x
        

def met_fun1(x):
    x=Rvns(x)
    while((time.time() - start_time)<30):
        k=0
        #cc=0
        while(k<3):
            # if k>4:
            #     k=0
            
     
            x1=N(x,k)
            l=0
            while(l<2):
                # c=0
                x2=N1(x1,l)
                a=val_obj_fun(x1)
                b=val_obj_fun(x2)
                if b<=a:
                    x1=x2[:]
                # c+=1
                # if c>3:
                #     l+=1
                l+=1
            val=val_obj_fun(x)
            #print('vvvvvvvvvv',val)
            if val>=b:
                x=x2[:]
            # cc+=1
            # if cc>3:
            #     k+1
            k+=1
    
    tt=[]
    c=0
    for j in x:
         tt.append([j[0],c,c+j[1]])
         c+=j[1]  
    return tt,val
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#                        metaheyristique   
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#                       objectif 2:
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
# les structures de voisinage deja defini  


def checkDelay22(lst, currentTime):
    if (currentTime) > lst[2]:
        return ( currentTime-lst[2])*lst[4]
    return (lst[2]-currentTime )*lst[3]






def val_obj_fun1(seq):
    val=0
    seqq=[]
    currentTime=0
    c=0
    for i in range(len(seq)):
        currentTime+=seq[i][1]
        seqq.append([seq[i][0],c,c+seq[i][1]])
        c+=seq[i][1]
        val+=checkDelay22(seq[i], currentTime)
        
    return val,seqq

start_time=time.time()
def met_fun(x):
    while((time.time() - start_time)<10):
        k=0
        while(k<3):
            x1=N(x,k)
            l=0
            while(l<3):
                x2=N1(x1,l)
                a=val_obj_fun1(x1)
                b=val_obj_fun1(x2)
                if b<a:
                    x1=x2[:]
                l+=1
            val=val_obj_fun1(x)
            if val>b:
                x=x2[:]
            k+=1
    #print(val)   
    return val  
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#                                             dynamique pro  
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#                                             objectif 1:
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
def checkDelay(lst, currentTime):
    if (lst[1] + currentTime) > lst[2]:
        return 1
    else:
        return 0
start_time = time.time()
def powerset(list_name):
     s = list(list_name)
     return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))



results = {}
seq={}
lst1=[]
identifier=''
def ff(t):
  return ",".join("'%s'" % a[0] for a in t)

# def currentTime(tmp):
#   currentTim=0
#   for index in range(0, len(tmp)):
#       currentTim +=tmp[index][1]
#   return currentTim


def recursionFunction(lst,id):
  if len(lst)==0:
    return 0
  else:
      #print(len(lst))
      global lst1
      global seq
      min = 177272
      for element in range(len(lst)):
          currentTime = 0
          temp=lst[:]
          temp.pop(element)
          for index in range(0, len(temp)):
              currentTime += temp[index][1]
      
          identifier =",".join("'%s'" % a[0] for a in temp)
          if identifier in results.keys():
              res=checkDelay(lst[element], currentTime)+results[identifier]
          else:
              res = checkDelay(lst[element], currentTime) + recursionFunction(temp,identifier)
          if res < min:
              min = res
              if len(temp)==0 :
                  seq[id]=[]
                  seq[id].append([lst[element][0],lst[element][1]])
              else:
                  # seq[id]=copy.deepcopy(seq[identifier])
                    seq[id]=seq[identifier][:]
                    seq[id].append([lst[element][0],lst[element][1]])

      return min
def fc_ob(data):
    global identifier
    for x in powerset(data):
    # for i in range(1,len(data)+1):
    #     sample = list(itertools.combinations(data, i))
    #     for iteam in sample:
            identifier =",".join("'%s'" % a[0] for a in x)
            results[identifier] = recursionFunction(list(x),identifier)
    # if len(iteam)>2:
    #     lst1 = list(seq.items())
    #     for i in range(0,math.comb(5,len(iteam)-3),1):
    #         del lst1[0]
    #     seq=copy.deepcopy(dict(lst1))
    c=0
    tt=[]
    for j in seq[identifier]:
        tt.append([j[0],c,c+j[1]])
        c+=j[1]
    lst = list(results.items())
    return lst[-1][1],tt

# lst = list(results.items())
# print(lst[-1][1])
# print(seq[identifier])
#print(seq)

print("--- %s seconds ---" % (time.time() - start_time))
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#                                             dynamique pro  
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#                                             objectif 2:
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

start_time = time.time()
def checkDelay1(lst, currentTime):
    if (lst[1] + currentTime) > lst[2]:
        return ( lst[1] + currentTime-lst[2])*lst[4]
    return (lst[2]-currentTime - lst[1] )*lst[3]


def powerset(list_name):
     s = list(list_name)
     return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

results = {}

seq={}
lst1=[]
def recursionFunction2(lst,id):
    global lst1
    global seq
    min = 177272
    if len(lst) != 0:
        for element in range(len(lst)):
            currentTime = 0
            temp=lst[:]
            temp.pop(element)
            for index in range(0, len(temp)):
                currentTime += temp[index][1]
            identifier = ",".join("'%s'" % a[0] for a in temp)
            if identifier in results.keys():
                res=checkDelay1(lst[element], currentTime)+results[identifier]
            else:
               res = checkDelay1(lst[element], currentTime) + recursionFunction2(temp,identifier)
            if res < min:
                min = res
                if len(temp)==0:
                    seq[id]=[]
                    seq[id].append([lst[element][0],lst[element][1]])
                else:
                     seq[id]=seq[identifier][:]
                     seq[id].append([lst[element][0],lst[element][1]])
        # if len(lst)>2:
        #     lst1 = list(seq.items())
        #     print(lst1)
        #     print('kkkkkkkkkkkkkkkkk',len(lst))
        #     print(math.comb(5,len(lst)-2))
        #     for i in range(0,math.comb(5,len(lst)-3),1):
        #         del lst1[0]
        #     print('======================',lst1)
        #     print('fin')
        #     seq=copy.deepcopy(dict(lst1))
        return min
    else:
        return 0
    
def fo_ob2(data):
     global identifier
     for x in powerset(data):
         identifier =",".join("'%s'" % a[0] for a in x)
         results[identifier] = recursionFunction2(list(x),identifier)
     lst = list(results.items())
     c=0
     tt=[]
     for j in seq[identifier]:
         tt.append([j[0],c,c+j[1]])
         c+=j[1]
     return lst[-1][1],tt
# for i in range(1,len(data)+1):
#     sample = list(itertools.combinations(data, i))
#     for iteam in sample:
#         identifier = ",".join("'%s'" % a[0] for a in iteam)
#         results[identifier] = recursionFunction(list(iteam),identifier)
    # if len(iteam)>2:
    #     lst1 = list(seq.items())
    #     for i in range(0,math.comb(5,len(iteam)-3),1):
    #         del lst1[0]
    #     seq=copy.deepcopy(dict(lst1))

lst = list(results.items())
# print(lst[-1][1])
# print(seq[identifier])
#print(seq)

# print("--- %s seconds ---" % (time.time() - start_time))