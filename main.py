import textblob as t
import sys


def wc(): 
    global g
    print("hello!") 
    g=input("who are you?")
    x=input("well, "+g+" how are you?") 

def lc(): 
    print("MultiCasE to lowercase")
    g=input("enter string") 
    c=g.lower() 
    print(g+"-->"+c) 

def ex():
    print("goodbye, "+g+" , see you again soon!")
    quit()

def uc(): 
    print("MultiCasE to UPPERCASE")
    a=input("enter string") 
    b=a.upper() 
    print(a+"-->"+b) 
    

def functs(): 
    print(''' 
    1)ascii art 
    2)just chat 
    3)MultiCasE to lowercase (/lowercase)
    4)MultiCasE TO UPPERCASE (/uppercase)
    enter /exit to exit at any time 
    enter /func to see this again''')
    

def nov():
    b=input("📎--")
    try:
        if b == "/exit":
            ex()
        if b == "/func":
            functs()
        if b == "/lowercase":
            lc()
        if b =="/uppercase":
            uc()
    except:
        print("an error occured")
    
wc() 
functs() 
while True:
    nov()
