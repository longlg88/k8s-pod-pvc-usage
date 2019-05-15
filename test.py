#!/usr/bin/python
import os
import sys
import subprocess

if __name__ == "__main__":
    result = subprocess.check_output("kubectl get pv --all-namespaces -o json | jq '.items[].status.phase'", shell=True)
    print("here : "+result)
    result=result.replace('"','')
    print(result.split("\n"))
    a=0
    result_list=result.split("\n")
    for s in result_list:
        print(type(s))
        if "Bound" == s:
            a=a+1
            a=str(a)
            cmd = "kubectl get pv --all-namespaces -o json | jq '.items[" + a + "].spec.claimRef.name'"
            print(cmd)
            name = subprocess.check_output(cmd, shell=True)
            print(name)