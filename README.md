# simple-minikube-deployment

## Overview

Simple test of Minikube deploying basic Hello World applications.

Tested on M1 Mac initially and partially on x86 Mac both running
the latest version of MacOS.


## Quick start 

See more detailed instructions below in the [setup](#Setup) section

* Install Docker
* Install minikube
* Start minikube (ensure ingress addon is enabled)
* Run following to build Docker image

```
cd service/python
make buildforminikube
cd ../..
```

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

Run this command in a seperate terminal to allow connection to the ingress

```
./ssh-tunnel.sh
```

then run a `curl` command to access the nginx server

```
curl -vvv -H "Host: hello.internal" localhost:10080/hello
```


## Setup 

### Installation 

This has been tested on an M1 Mac and an old x86 Mac, both running 
MacOS 12.4.


#### Docker

Downloading [docker desktop](https://www.docker.com/products/docker-desktop/)

Start Docker Desktop from the Launcher


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


### Development 

#### Python setup

Using Python3 run the following commands under `service/python`

```
python3 -mvenv .matrix
. .matrix/bin/activate
pip install -r requirements
```

To setup the initial packages needed for the code ran this:

```
pip install flask && pip freeze > requirements.txt
```

#### Testing Service 

The service can be run locally with either 

* `python service.py`
* `./service.py`

You can test it's working using curl 

```
curl -vvv 'http://localhost:5000?name=sheila'
```


#### Local Docker image

You can build the docker image for the service using the local Docker 
daemon using the following command

```
make buildforlocal
```

You can then start a Docker container using the following command

```
docker run -it -p 5173:8173 pythonhello:0.1.3
```

Test using curl in another window (the above doesn't detach from the 
terminal)

```
curl -vvv 'http://localhost:5173?name=Vimes'
```

The container can be terminated using CTRL-C in the terminal used 
to run the docker command above.


#### Minikube Docker Image

This can be built using the following

```
make buildforminikube
```

You can check that the image has been built using 

```
make checkminikubeimages
```


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


### Getting SSH Command

The `minikube tunnel` command requires admin rights - I don't like this.  The 
`minikube service` command can be used to create a tunnel but this just picks
random ports, for example I ran this twice, one after the other and got this

```
ps -ef | grep docker@127.0.0.1
  502 78255 62117   0  9:39am ttys014    0:00.00 grep ssh
  502 78247 78234   0  9:39am ttys015    0:00.01 ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -N docker@127.0.0.1 -p 56635 -i /Users/fiona/.minikube/machines/minikube/id_rsa -L 60101:10.101.8.218:80 -L 60102:10.101.8.218:443
```

Then this

```
ps -ef | grep docker@127.0.0.1
  502 78417 62117   0  9:44am ttys014    0:00.00 grep docker@127.0.0.1
  502 78389 78376   0  9:43am ttys015    0:00.01 ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -N docker@127.0.0.1 -p 56635 -i /Users/fiona/.minikube/machines/minikube/id_rsa -L 60180:10.101.8.218:80 -L 60181:10.101.8.218:443
```

Using the above I was able to create the `ssh-tunnel.sh` script that does 
essentially the same thing but uses known ports for redirecting to the 
LoadBalancer endpoint for minikube.


## References

### k8s Manifests

* [Creating a pod](https://kubernetes.io/docs/concepts/workloads/pods/)
* [Creating a namespace](https://cloud.google.com/blog/products/containers-kubernetes/kubernetes-best-practices-organizing-with-namespaces)
* [Services](https://kubernetes.io/docs/concepts/services-networking/connect-applications-service/)
* [Ingress](https://kubernetes.io/docs/concepts/services-networking/ingress/)
* [Define environment variables for container](https://kubernetes.io/docs/tasks/inject-data-application/define-environment-variable-container/)


### k8s

* [Ingress](https://kubernetes.io/docs/concepts/services-networking/ingress/)
* [Connecting applications with services](https://kubernetes.io/docs/concepts/services-networking/connect-applications-service/)

### Minikube

* [Accessing applications](https://minikube.sigs.k8s.io/docs/handbook/accessing/)
* [Minikube github repo](https://github.com/kubernetes/minikube)
* [Setup Ingress controller](https://kubernetes.io/docs/tasks/access-application-cluster/ingress-minikube/)
* [Howto use local docker images with minikube](https://stackoverflow.com/questions/42564058/how-to-use-local-docker-images-with-minikube)
* [README section on using minikube docker for images](https://github.com/kubernetes/minikube/blob/0c616a6b42b28a1aab8397f5a9061f8ebbd9f3d9/README.md#reusing-the-docker-daemon)


### Docker 

* [Accessing HyperKit VM for Docker Desktop on Mac](https://stackoverflow.com/questions/39739560/how-to-access-the-vm-created-by-dockers-hyperkit)
* [Image for nginx](https://hub.docker.com/_/nginx)
* [Docker and localhost](https://stackoverflow.com/questions/24319662/from-inside-of-a-docker-container-how-do-i-connect-to-the-localhost-of-the-mach)
* [Docker ps docs](https://docs.docker.com/engine/reference/commandline/ps/)


### Homebrew

* [List all files in Homebrew package](https://stackoverflow.com/questions/19010784/list-all-files-in-a-homebrew-package)


### Ingress Controllers

* [Advanced nginx configuration with annotations](https://docs.nginx.com/nginx-ingress-controller/configuration/ingress-resources/advanced-configuration-with-annotations/)
* [Artifact hub - ingress-nginx](https://artifacthub.io/packages/helm/ingress-nginx/ingress-nginx)
* [Change ports ingress controller uses](https://stackoverflow.com/questions/57926545/change-kubernetes-nginx-ingress-controller-ports)


### Python

* [Creating requirements.txt from pip](https://stackoverflow.com/questions/19135867/what-is-pips-equivalent-of-npm-install-package-save-dev)
* [Official Docker image](https://hub.docker.com/_/python)
* [Flask on pypi](https://pypi.org/project/Flask/)
* [Flask documentation](https://flask.palletsprojects.com/en/2.1.x/)
* [How to run a flask application](https://www.twilio.com/blog/how-run-flask-application)
* [Return JSON from Flask](https://stackoverflow.com/questions/13081532/how-to-return-a-dict-as-a-json-response-from-a-flask-view)
* [Change host and port on Flask](https://stackoverflow.com/questions/41940663/how-can-i-change-the-host-and-port-that-the-flask-command-uses)


### Makefile

* [Using variables](https://ftp.gnu.org/old-gnu/Manuals/make-3.79.1/html_chapter/make_6.html)
* [Phony targets](https://www.gnu.org/software/make/manual/html_node/Phony-Targets.html)
* [Adding help for Makefile targets](https://gist.github.com/prwhite/8168133)
* [Improved help generator](https://www.freecodecamp.org/news/self-documenting-makefile/)


### Shell

* [Running SSH without shell](https://unix.stackexchange.com/questions/100859/ssh-tunnel-without-shell-on-ssh-server)
* 
