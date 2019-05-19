## sidecar pattern
#### volumeMounts 값을 sidecar pod에 붙일 것과 맞추자

## 클러스터 안에서 kube-api가 동작 하는가?
#### kube-api가 동작하려면 kube-config가 있고, 어떤 pod에 명령을 내릴지 즉 모든 namespace의 pod를 볼 수 있는 권한이 있어야 할 것 같은데...

## 현재 개발 요건이 어떻게 되는가?
 
#### 가장 쉽게 하는 방법 --> 확인해볼것
#### efs-provisioner와 같은 volume mount path
#### 접근해서 pv 이름을 parsing
#### parsing 받은 pv이름을 split해서 앞단이 namespace나 pod name과 같은지 확인 --> namespace or pod-name --> this value, we is called target
#### 뭐와 같은 값이냐에 따라서 du 값과 target값을 묶어서 prometheus로 전송
#### 값만 추출가능하면 prometheus로 보내는 client 구현 가능