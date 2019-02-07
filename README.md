# LDAPie -A tool to bruteforce LDAP attributes in python

# Requirements:

- Python2.7 <b>(NOT TESTED ON 3)</b>
- requests

# Notes

Since it's still being worked out and since I don't really know python all that well there are some bugs<br>
feel free to let me know so I can fix them, also feel free to let me know how it's working for you<br>

# Usage
python LDAPie.py -w <wordlist> -g/p <get/post> -u <url>

Example:

python LDAPie.py -w gd.txt -p -u http://gd.com/path/to/form<br>
python LDAPie.py -w gd.txt -g -u http://gd.com/path/to/form
