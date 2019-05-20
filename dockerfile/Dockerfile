# Dockerfile
FROM alpine

ENV KUBE_LATEST_VERSION="v1.14.2"

RUN apk add -v --update curl bash jq git ca-certificates python3 python3-pip\
  && curl -L https://storage.googleapis.com/kubernetes-release/release/${KUBE_LATEST_VERSION}/bin/linux/amd64/kubectl -o /usr/local/bin/kubectl \
  && chmod +x /usr/local/bin/kubectl

COPY / /root
CMD ["/root/test.sh"]
