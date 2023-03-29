import textblob as t
import sys,random,re,string

g=""
=======
import sys
def wc(): 
    print("hello!") 
    g=input('''who are you?
    📎-- ''')
    x=input('''well, "+g+" how are you? 
    📎-- ''') 
    print("i'm also "+x+" too!")

def lc(): 
    print("MultiCasE to lowercase")
    g=input("enter string") 
    c=g.lower() 
    print(g+"-->"+c) 

def ex():
    print("goodbye, "+g+" , see you again soon!")
    sys.exit(0)

def uc(): 
    print("MultiCasE to UPPERCASE")
    a=input("enter string") 
    b=a.upper() 
    print(a+"-->"+b) 
    

def functs(): 
    print(''' 
    there are many functions avalible
    1)ascii art (/ascii)
    2)just chat 
    3)MultiCasE to lowercase (/lowercase)
    4)MultiCasE TO UPPERCASE (/uppercase)
    enter /exit to exit at any time 
    enter /func to see this again''')
    

def nov():
    b=input("📎--")
    if b == "/exit":
        ex()
    try:    
        if b == "/func":
            functs()
        if b == "/lowercase":
            lc()
        if b =="/uppercase":
            uc()
        if b == "/ascii":
            print('''
                _        ____                                 _       ____      _____   
U  /"\  u U /"___|    ___         ___         U  /"\  uU |  _"\ u  |_ " _|  
 \/ _ \/  \| | u     |_"_|       |_"_|         \/ _ \/  \| |_) |/    | |    
 / ___ \   | |/__     | |         | |          / ___ \   |  _ <     /| |\   
/_/   \_\   \____|  U/| |\u     U/| |\u       /_/   \_\  |_| \_\   u |_|U   
 \\    >>  _// \\.-,_|___|_,-.-,_|___|_,-.     \\    >>  //   \\_  _// \\_  
(__)  (__)(__)(__)\_)-' '-(_/ \_)-' '-(_/     (__)  (__)(__)  (__)(__) (__) 
what did you expect? 📎📎📎
            ''')
    except:
        print("an error occured")
    
wc() 
functs() 
while True:
    nov()
