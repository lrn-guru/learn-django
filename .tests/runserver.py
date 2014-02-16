#!/usr/bin/env python
import requests

try:
    r = requests.get('http://localhost:8000')
    exit(0)
except requests.ConnectionError:
    exit(1)
