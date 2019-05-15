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
        # check if pv is "Bound"
        if "Bound" == s:
            a=a+1
            a=str(a)
            ## find name / namespace for pv which is "Bound"
            name_cmd = "kubectl get pv --all-namespaces -o json | jq '.items[" + a + "].spec.claimRef.name'"
            name = subprocess.check_output(name_cmd, shell=True).replace('\n','')
            namespace_cmd = "kubectl get pv --all-namespaces -o json | jq '.items[" + a + "].spec.claimRef.namespace'"
            namespace = subprocess.check_output(namespace_cmd, shell=True)#.replace('\n','')
            a=int(a)
            # print(name + " " + namespace)
    ## remove duplicate values
    namespace_list=namespace.split("\n")
    namespace_list = list(set(namespace))

    for val in namespace_list:
        ## 
        mount_pod_cmd = "kubectl describe pvc -n " + val + " | grep Mounted | awk '{print $3}'"
        mount_pod = subprocess.check_output(mount_pod_cmd, shell=True)
        print(mount_pod)