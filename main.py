import textblob as t
import sys,random,re,string


import sys
def wc():
    global g 
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
      >>         >=>>=>       >=>    >=> >=>                             >=>   
     >>=>      >=>    >=>  >=>   >=> >=> >=>                             >=>   
    >> >=>      >=>       >=>        >=> >=>          >=> >=>  >> >==> >=>>==> 
   >=>  >=>       >=>     >=>        >=> >=>        >=>   >=>   >=>      >=>   
  >=====>>=>         >=>  >=>        >=> >=>       >=>    >=>   >=>      >=>   
 >=>      >=>  >=>    >=>  >=>   >=> >=> >=>        >=>   >=>   >=>      >=>   
>=>        >=>   >=>>=>      >===>   >=> >=>         >==>>>==> >==>       >=> 
what did you expect? 📎📎📎
            ''')
    except:
        print("an error occured")
    
wc() 
functs() 
while True:
    nov()
