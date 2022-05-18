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

## Setup 

### Installation 

This has been tested on an M1 Mac

#### Docker

Downloading [docker desktop](https://www.docker.com/products/docker-desktop/)

Start Docker Desktop


#### Homebrew

The easiest way to get many of the scripts and utilies is to use
[homebrew](https://brew.sh) I've followed the [untar anywhere](https://docs.brew.sh/Installation#untar-anywhere) approach as this doesn't require admin rights
and hopefully doesn't risk damage to my system.

Also the `$PATH` variable is set with homebrew at the end so it can't override 
anything that may be important from a security point of view


#### Minikube

Installed using homebrew

```
brew install minikube
```

Also added `kubectx` as this is useful to avoid long `kubectl` command that 
require the context and namespace being specified all the time

```
brew install kubectx
```


### Startup

#### Minikube

Start minikube using the following command

```
minikube start --driver=docker
```

Enable the ingress addon

```
minikube addons enable ingress
```

TODO: Fix ingress so it doesn't need 80/443 which are privileged ports


## Troubleshooting

### Minikube Ingress controller not running

When applying the deployment you get this result

```
kubectl get ingress
NAME            CLASS           HOSTS   ADDRESS   PORTS   AGE
hello-ingress   nginx-example   *                 80      6m16
```

Check the ingress controller is running

```
kubectl get pods -n ingress-nginx
```

If this returns no pods, then delete the ingress and check the instructions
above for startup of minikube to ensure the ingress addon is running

```
kubectl delete ingress hello-ingress
```



## References

### k8s Manifests

* [Creating a pod](https://kubernetes.io/docs/concepts/workloads/pods/)
* [Creating a namespace](https://cloud.google.com/blog/products/containers-kubernetes/kubernetes-best-practices-organizing-with-namespaces)
* [Services](https://kubernetes.io/docs/concepts/services-networking/connect-applications-service/)
* [Ingress](https://kubernetes.io/docs/concepts/services-networking/ingress/)

### Minikube

* [Ingress controller]()
