#!/usr/bin/python
import os
import sys
import subprocess

if __name__ == "__main__":
    # result = subprocess.check_output("kubectl get pv --all-namespaces -o json | jq '.items[].status.phase'", shell=True)
    result = subprocess.run("kubectl get pv --all-namespaces -o json | jq '.items[].status.phase'", stdout=subprocess.PIPE)
    print("here : "+result.stdout.decode('utf-8'))
    result=result.stdout.decode('utf-8')
    result=result.replace('"','')
    print(result.split("\n"))
    a=0
    result_list=result.split("\n")
    for s in result_list:
        if "Bound" == s:
            a=a+1
            a=str(a)
            cmd = "kubectl get pv --all-namespaces -o json | jq '.items[" + a + "].spec.claimRef.name'"
            # name = subprocess.check_output(cmd, shell=True)
            name = subprocess.run(cmd, stdout=subprocess.PIPE).stdout.decode('utf-8')
            # name = os.system(cmd)
            print(name)
            a=int(a)