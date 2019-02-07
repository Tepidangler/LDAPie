# LDAPie -A tool to bruteforce LDAP attributes in python

# Requirements:

- Python 2.7 or 3.6

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

Since it's still being worked out and since I don't really know python all that well there
are some bugs.

Feel free to let me know so I can fix them, also feel free to let me know how it's working for you.

# Usage
python ldapie -w <wordlist> -g/p <get/post> -u <url>

Example:

```
    python ldapie -w gd.txt -m "get" -u http://gd.com/path/to/form
    python ldapie -w gd.txt -m "post" -u http://gd.com/path/to/form
```
