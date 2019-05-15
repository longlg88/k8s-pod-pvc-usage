#!/usr/bin/python
import os
import sys

if __name__ == "__main__":
    result = os.system("kubectl get pv --all-namespaces -o json | jq '.items[].status.phase'")
    print(result)