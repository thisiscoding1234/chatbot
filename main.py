import textblob as t
import sys,random,re,string

def wc(): 
    print("hello!") 
    g=input("who are you?")
    x=input("well, "+g+" how are you?") 

def lc(): 
    print("MultiCasE to lowercase")
    g=input("enter string") 
    c=g.lower() 
    print(g+"-->"+c) 

def uc(): 
    print("MultiCasE to UPPERCASE")
    a=input("enter string") 
    b=a.upper() 
    print(a+"-->"+b) 

def functs(): 
    d=90
    d=int(input(''' 
    1)ascii art 
    2)just chat 
    3)MultiCasE to lowercase 
    4)MultiCasE TO UPPERCASE 
    5) 
    6) 
    7) 
    8) 
    9) 
    plese enter one of the numbers '''))
    if d==3: 
        lc()
    elif d==4:
        uc()
    

wc() 
functs() 