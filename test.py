#!/usr/bin/python3
import os
import sys

if __name__ == "__main__":
    result = os.system("k get pv --all-namespaces -o json | jq '.items[].status.phase'")
    print(result)