#!/usr/bin/python36

import subprocess as sp
import cgi

print("content-type: text/html")
print()

form=cgi.FieldStorage()

docker_name=form.getvalue("n")
docker_image=form.getvalue("img")

docker_run="sudo docker run -d -it --name {} {}".format(docker_name, docker_image)

x=sp.getoutput(docker_run)

print(x)
