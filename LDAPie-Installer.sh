#!/bin/bash

GITC=$(which git)
PYTHON=$(which python)

${GITC} clone https://github.com/Tepidangler/LDAPie.git

cd LDAPie

${PYTHON} setup.py bdist_wheel
mkdir -p ${HOME}/.ldapie
mv wordlist ${HOME}/.ldapie
cd dist/
${PYTHON} -m pip install *.whl --user

mkdir -p $HOME/.local/bin
echo "${PYTHON} ldapie" > $HOME/.local/bin/ldapie
