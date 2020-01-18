key=['Q','A','Z','X','S','W','E','D','C','V','F','R',
     'T','G','B','N','H','Y','U','J','M','K','I','O','L','P']
print('key')
print(key)

key1=[]
key2=[]
key3=[]
import random
while len(key)>0:
    i=random.randint(0,len(key)-1)
    key1.append(key[i])
    del(key[i])
print('key1')
print(key1)
key=['Q','A','Z','X','S','W','E','D','C','V','F','R',
     'T','G','B','N','H','Y','U','J','M','K','I','O','L','P']
while len(key)>0:
    i=random.randint(0,len(key)-1)
    key2.append(key[i])
    del(key[i])
print('key2')
print(key2)
key=['Q','A','Z','X','S','W','E','D','C','V','F','R',
     'T','G','B','N','H','Y','U','J','M','K','I','O','L','P']
while len(key)>0:
    i=random.randint(0,len(key)-1)
    key3.append(key[i])
    del(key[i])
print('key3')
print(key3)
