# simple-minikube-deployment

## Overview




## Quick start 

* Install Docker
* Install minikube
* Start minikube
* Run the following to create the deployment

```
kubectl apply -f deployment.yaml
```

Check with the following command

```
kubens helloworld
kubectl get pods
kubectl get svc
```

## Installation 

This has been tested on an M1 Mac

### Docker

Downloading [docker desktop](https://www.docker.com/products/docker-desktop/)

Start Docker Desktop


### Homebrew

The easiest way to get many of the scripts and utilies is to use
[homebrew](https://brew.sh) I've followed the [untar anywhere](https://docs.brew.sh/Installation#untar-anywhere) approach as this doesn't require admin rights
and hopefully doesn't risk damage to my system.

Also the `$PATH` variable is set with homebrew at the end so it can't override 
anything that may be important from a security point of view


### Minikube

Installed using homebrew

```
brew install minikube
```

Also added `kubectx` as this is useful to avoid long `kubectl` command that 
require the context and namespace being specified all the time

```
brew install kubectx
```



## References

### k8s Manifests

* [Creating a pod](https://kubernetes.io/docs/concepts/workloads/pods/)
* [Creating a namespace](https://cloud.google.com/blog/products/containers-kubernetes/kubernetes-best-practices-organizing-with-namespaces)
* [Services](https://kubernetes.io/docs/concepts/services-networking/connect-applications-service/)
