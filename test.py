#!/usr/bin/python
import os
import sys
import subprocess

if __name__ == "__main__":
    result = subprocess.check_output("kubectl get pv --all-namespaces -o json | jq '.items[].status.phase'", shell=True)
    print("here : "+result)
    print(result.split("\n"))
    result_list=result.split("\n")
    a=0
    if "Bound" in result_list:
        a=a+1
        print(a)
    else:
        print(a)