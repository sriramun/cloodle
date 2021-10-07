#!/usr/bin/env python3

import sys
import json


try: 
    print(json.load(sys.stdin)[sys.argv[1]]) 

except: 
    print("")
