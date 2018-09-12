from pickaword import *
from guessletters import *
from bela import get_answer
import sys

def main():
    welcome= """
    Welcome to Hangman!
    
    Instructions:
        - the computer will choose a word randomly from a list
        - you have to guess it letter by letter
        - after 5 wrong letters you will be hanged up
        
        - to quit any time just push Ctrl+C and then ENTER
        
    Have FUN!
    
        
        """
    
    bye="""
        
        I hope it was good!
        
        ByeBye!"""
    
    print(welcome)
    input("Press ENTER if you want to start...")
    
    cont = True
    while cont:
        w = pick().lower()
        guess(w)
        cont=get_answer("Do you want to play again? (y/n)")
        if not cont:
            print(bye)
            sys.exit()
    


    

if __name__ == '__main__':
    main()
    
