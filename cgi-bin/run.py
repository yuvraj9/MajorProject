#!/usr/bin/python36

import subprocess as sp
import cgi

print("content-type: text/html")
print()

cmd="sudo docker ps -a"
output=sp.getoutput(cmd)
container_list=output.split("\n")
form=cgi.FieldStorage()

print("<iframe width='100%' name='myconsole'></iframe>")
print("""
<table border="5" width='100%'>
<tr>
<th>Conatainer Name</th>
<th>Image Name</th>
<th>Status</th>
<th>Start</th>
<th>Stop</th>
<th>Terminate</th>
<th>Console</th>
</tr>""")
for c in container_list[1:]:
	if "Up" in c:
		cstatus="running"
	elif "Exited" in c:
		cstatus="stopped"
	else:
		status="unknown status"
	c_details=c.split()
	cname=c_details[-1]
	imagename=c_details[1]
	print(
	"""
	<tr>
	<td>{}</td>
	<td>{}</td>
	<td>{}</td>
	<td><a href='http://192.168.43.171/cgi-bin/docker_start.py?s={}'>Start</a></td>
	<td><a href='http://192.168.43.171/cgi-bin/docker_stop.py?s={}'>Stop</a></td>
	<td><a href='http://192.168.43.171/cgi-bin/docker_terminate.py?s={}'>Terminate</a></td>
	<td><a target='myconsole' href='http://192.168.43.171:4200'>Console</a></td>
	</tr>
	""".format(cname,imagename,cstatus,cname,cname,cname))

print("</table>")
