#!/bin/bash
#yum install openssh-server -y
mkdir /root/.ssh/
ssh-keygen -t rsa -P '' -f id_rsa
cp /id_rsa /id_rsa.pub /root/.ssh/
yum install epel-release -y
yum install sshpass -y
sshpass -p "redhat" ssh-copy-id -o StrictHostKeyChecking=no root@192.168.99.101
