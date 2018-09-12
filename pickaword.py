import random

def pick():
    with open('sowpods.txt','r') as dictio:
        dictio = "".join([dictio.readline() for i in dictio]).splitlines()
        
    l=len(dictio)
    r = random.randint(0,l)
    word = dictio[r]
    return word



    

