#!/usr/bin/env python3
# Download a web page using the requests module

import requests

res = requests.get('https://automatetheboringstuff.com/chapter11/')
print(res.text[:250])
