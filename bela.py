# selected collection of useful funcions

def get_integer(text="Give me a number: "):
    n = input(text)
    while n is not int:
        try:
            n = int(n)
            break
        except:
            n = input("It was not an integer please retry: ")
            continue
    return n


def get_divisors(n):
    try:
        n = int(n)
        return [i for i in range(1,n+1) if n%i == 0]
    except:
        print ("the argument is not an integer")
        
        
        
def get_intersection(l1,l2):
    from numpy import random
    try:
        return set(l1).intersection(set(l2))
    except:
        print ("They are maybe not lists, or other bug happend")


def if_palindrome(text):
    try:
        text = str(text)
        if text == "":
            print("the string is empty")
        else:
            if text == text[::-1]:
                print("Your string is a palindrome")
            else:
                print("It is not a palindrome")
    except:
        print("The argument is not a string, or it's empty")
        

def isaprime(n):
    try:
        n=int(n)
        if len([i for i in range(1,n+1) if n%i == 0])==2:
            return True
        else:
            return False
    except:
        print("the argument is not an integer")


def list_ends(l):
    if type(a) is list:
        return [l[:1],l[-1:]]
    else:
        print ("argument type is not a list")
        
        
def remove_duplic(l):
    single = []
    [single.append(i) for i in l if i not in single]
    return single
    
def remove_duplicset(l):
    return list(set(l))
    
    
    
def reverse_sentence(text="Give me a sentence: "):
    s = input(text)
    while type(s) is not str or len(s.split())<3:
        s = input("It was too short, or argument was not a srting \n Please retry:")
    else:
        back=""
        for i in s.split()[::-1]:
            back += i + " "
    return back



def get_answer(text="Yes or no? (y/n): ",lis=["y","n"]):
    inp = input(text)
    while inp not in lis:
        inp = input("Please type '%s' or'%s': " % (lis[0],lis[1]))
    if inp==lis[0]:
        return True
    elif inp==lis[1]:
        return False
        

def generator_weak():
    lis = [
        "qwerty",
        "asdfg",
        "11111111",
        "00000000",
        "admin"
        ]
    from numpy import random
    return lis[random.randint(0,len(lis))]



def generator_hard(x):
    from numpy import random
    import string
    import numpy as np
    p = int (x/4)
    m = x%4

    low = list(random.choice(list(string.ascii_lowercase),p))
    high = list(random.choice(list(string.ascii_uppercase),p))
    dig = list(random.choice(list(string.digits),p))
    pun = list(random.choice(list(string.punctuation),p))
    all = list(random.choice(list(string.printable),m))
    
    pas = low + high + dig + pun + all
    print(pas)
    random.shuffle(pas)
    
    fin = "".join(pas)
    return fin            
    
def number_generator(l):
    import string
    import random
    s = random.sample(range(1,10),1) + random.sample(range(10),l-1)
    return int("".join(str(x) for x in s))





