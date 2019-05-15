#!/usr/bin/python
import os
import sys
import subprocess

if __name__ == "__main__":
    result = subprocess.check_output("kubectl get pv --all-namespaces -o json | jq '.items[].status.phase'", shell=True)
    result=result.replace('"','')
    a=0
    result_list=result.split("\n")
    namespace_list=[]
    for s in result_list:
        ## check if pv is "Bound"
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
            namespace=''.join(namespace.split("\n"))
            namespace_list.append(namespace)

    ## remove duplicate values
    mount_pod_list=[]
    mount_path_list=[]
    namespace_list = list(set(namespace_list))
    for val in namespace_list:
        ## find pod mounted
        print("val = "+val)
        mount_pod_cmd = "kubectl describe pvc -n " + val + " | grep Mounted | awk '{print $3}'"
        mount_pod = subprocess.check_output(mount_pod_cmd, shell=True)
        # print(mount_pod)
        mount_pod=mount_pod.split("\n")
        print(mount_pod)
        for m_path in mount_pod:
            ## find mountPath in pod
            if m_path != "<none>":
                if m_path:
                    #mount_pod_list.append(mount_pod)
                    mount_path_cmd = "kubectl get pod -n " + val + " " + m_path + " -o json | jq '.spec.containers[0].volumeMounts[].mountPath'"
                    mount_path=subprocess.check_output(mount_path_cmd, shell=True)
                    ## append list in list
                    print("path = " + mount_path)
                    mount_path_list.append(mount_path)
            else:
                continue

    print(mount_path_list)
