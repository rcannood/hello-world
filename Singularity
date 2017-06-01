Bootstrap: docker
From: ubuntu:14.04

%labels
MAINTAINER vanessasaur

%environment
DINOSAUR=vanessasaurus
export DINOSAUR

%files
rawr.sh /rawr.sh

%runscript
exec /bin/bash /rawr.sh
