#! python

# pw.py - an insecure password locker program

# to use: py pw.py email
# and then ctrl+v to paste

PASSWORDS = {'email': 'lkfaj83FjfLKD89sLJ', 'blog': 'ow83Jdlk839lkKDKD', 'luggage': '12345'}

import sys, pyperclip

if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]       #first command line arg is the account name
if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)
    