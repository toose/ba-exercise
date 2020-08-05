#!/usr/bin/env python3

import re
import requests
import sys

def main(URI):
    ip_list = []

    try:
        response = requests.get(URI)
        response.raise_for_status()
    except Exception as execinfo:
        print(str(execinfo.args[0]))
        sys.exit(1)

    for line in response.text.splitlines():
        match = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', line)
        if match:
            ip_list.append(match.group())
    
    print(set(ip_list))


if __name__ == '__main__':
    main(sys.argv[1])