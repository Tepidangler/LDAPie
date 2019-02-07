# LDAPie -A tool to bruteforce LDAP attributes in python

# Requirements:

- Python2.7 <b>(NOT TESTED ON 3)</b>
- requests

# Installing

```
    git clone <url>
    python setup.py bdist_wheel
    cd dist/
    pip install *.whl
```

You can test `ldapie` with:

```
    python ldapie -h
```


# Notes

Since it's still being worked out and since I don't really know python all that well there are some bugs<br>
feel free to let me know so I can fix them, also feel free to let me know how it's working for you<br>

# Usage
python ldapie -w <wordlist> -g/p <get/post> -u <url>

Example:

python ldapie -w gd.txt -m "get" -u http://gd.com/path/to/form<br>
python ldapie -w gd.txt -m "post" -u http://gd.com/path/to/form
