import string


def get_letter():
    g = input("Guess your letter:")
    while g not in string.ascii_letters:
            g = input("That was not a letter:")
    return g



def drawmen(n):
    s6="""
        __________
        |        |
       ( )       |
        |        |
       /|\       |
      / | \      |
        |        |
       / \       |
     _/   \_     |
               __|__
     """
    s5="""
        __________
        |        |
       ( )       |
        |        |
       /|\       |
      / | \      |
        |        |
       /         |
     _/          |
               __|__
     """
    s4="""
        __________
        |        |
       ( )       |
        |        |
       /|\       |
      / | \      |
        |        |
                 |
                 |
               __|__
     """
    s3="""
        __________
        |        |
       ( )       |
        |        |
       /|        |
      / |        |
        |        |
                 |
                 |
               __|__
     """
    s2="""
        __________
        |        |
       ( )       |
        |        |
        |        |
        |        |
        |        |
                 |
                 |
               __|__
     """
    s1="""
        __________
        |        |
       ( )       |
                 |
                 |
                 |
                 |
                 |
                 |
               __|__
     """
    s0="""
        __________
        |        |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
               __|__
     """
    
    if n==6:
        return s6
    elif n==5:
        return s5
    elif n==4:
        return s4
    elif n==3:
        return s3
    elif n==2:
        return s2
    elif n==1:
        return s1
    elif n==0:
        return s0



def guess(w):
    w.lower()
    mis=0
    lis = []
    monitor = list("-"* len(w))
    
    while True:
        print(drawmen(mis))
        if lis:
            print("".join(monitor),"           Used letters: %s" % ", ".join(lis))
        else:
            print("".join(monitor))
        
        if "-" not in monitor:
            print("You found it!")
            break
        elif mis>5:
            print("You are hanged up, sorry!")
            print("The word was: %s" % w)
            break
            
        g = get_letter().lower()
    
        if g in w:
            i=0
            for v in w:
                if v == g:
                    monitor[i]=g
                i+=1
        elif g in "".join(lis) :
            print("This is duplicate")
        else:
            mis+=1
            lis.append(g)
        


