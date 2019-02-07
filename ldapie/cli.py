import click
from colorama import (
    Fore,
    Back,
    Style,
)
from pyfiglet import Figlet
from lib import LDAPie
from multiprocessing import Pool
try:
    from pathlib import Path
except:
    from os.path import (
        abspath,
        expanduser,
    )


fig = Figlet(font='slant')
LOGO = fig.renderText('LDAPie')
WELCOME = '''#####################################################
    Welcome to LDAPie by Tepidangler
    Email: tepidangler@protonmail.com
    Info: This is a program created out of 
          necessity since I couldn't find a
          program that did LDAP injection
          via POST requests
    TODO: loosen up request params, automate
          IF URL IS NOT SET YOU WILL GET FALSE NEGATIVES :)
#####################################################
'''
try:
    LDAPIE_HOME = str(Path.home())
except:
    LDAPIE_HOME = expanduser('~')
LDAPIE_HOME = LDAPIE_HOME + '/.ldapie'


def get(line, url):
    data = LDAPie.get(line, url)
    if data['is_valid']:
        print(Back.GREEN
              + Fore.WHITE
              + Style.BRIGHT
              + ' VALID LDAP INJECTION '
              + Style.RESET_ALL
              + ' '
              + data['url'])

def post(line, url):
    data = LDAPie.get(line, url)
    if data['is_valid']:
        print(Back.GREEN
              + Fore.WHITE
              + Style.BRIGHT
              + ' VALID LDAP INJECTION '
              + Style.RESET_ALL
              + ' '
              + data['inputUsername'])

@click.command()
@click.option('-w', '--wordlist', default=LDAPIE_HOME + '/wordlist', help='Path to the word list file')
@click.option('-u', '--url', help='The LDAP endpoint to check')
@click.option('-m', '--method', default='get', help='The HTTP method to use')
def main(wordlist, url, method):
    try:
        try:
            wordfile = Path(wordlist).resolve()
        except:
            wordfile = abspath(wordlist)
        lines = []
        with open(wordfile, 'r') as f:
            lines = f.read().splitlines()

        if url is None:
            raise ValueError('URL cannot be value {}.'.format(url))

        args = [(line, url) for line in lines]

        parsed_method = method.lower()

        print(Fore.YELLOW + LOGO + Style.RESET_ALL + '\r\n')
        print(Fore.CYAN + Style.BRIGHT + WELCOME + Style.RESET_ALL)

        responses = None
        response_key = None
        print(
            Back.CYAN
            + Style.BRIGHT
            + ' INFO '
            + Style.RESET_ALL
            + ' '
            + 'Making a {0} request to {1}'.format(parsed_method.upper(), url.lower())
            + '\r\n\r\n'
        )

        with Pool() as p:
            if parsed_method == 'post':
                responses = p.starmap(LDAPie.post, map(lambda l: (l, url,), lines))
            else:
                responses = p.starmap(get, args)
    except ValueError as e:
        print(Back.RED
              + Style.BRIGHT
              + ' ERROR '
              + Style.RESET_ALL
              + ' '
              + str(e))
