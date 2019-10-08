#!/usr/bin/python36
import subprocess as sp
import cgi
print("content-type: text/html")
print()
mydata=cgi.FieldStorage()
y=mydata.getvalue('q')
if "shell" and  "box" in y:
	print("<meta http-equiv='refresh' content='0;url=http://192.168.43.171/shellinabox.html'/>")
elif "command" in y:
        print("<meta http-equiv='refresh' content='0;url=http://192.168.43.171/cgi-bin/command.py'/>")
elif "install" and "software" in y:
	print("<meta http-equiv='refresh' content='0;url=http://192.168.43.171/cgi-bin/package.py'/>")
elif "start" and "service" in y:
        print("<meta http-equiv='refresh' content='0;url=http://192.168.43.171/cgi-bin/service.py'/>")
elif "start" and "service" in y:
        print("<meta http-equiv='refresh' content='0;url=http://192.168.43.171/cgi-bin/service.py'/>")
elif "stop" and "service" in y:
        print("<meta http-equiv='refresh' content='0;url=http://192.168.43.171/cgi-bin/stop_service.py'/>")
elif "send" and "mail" in y:
        print("<meta http-equiv='refresh' content='0;url=http://192.168.43.171/cgi-bin/mail.py'/>")
elif "launch" and "container" in y:
        print("<meta http-equiv='refresh' content='0;url=http://192.168.43.171/cgi-bin/d.py'/>")
elif "manage" and "container" in y:
        print("<meta http-equiv='refresh' content='0;url=http://192.168.43.171/cgi-bin/run.py'/>")
elif "make" and "archive" in y:
        print("<meta http-equiv='refresh' content='0;url=http://192.168.43.171/cgi-bin/archive.py'/>")
elif "launch" and "instance" in y:
        print("<meta http-equiv='refresh' content='0;url=http://192.168.43.171/cgi-bin/ec2.py'/>")
elif "build" and "bucket" in y:
        print("<meta http-equiv='refresh' content='0;url=http://192.168.43.171/cgi-bin/s3.py'/>")
elif "hadoop" and "cluster" in y:
        print("<meta http-equiv='refresh' content='0;url=http://192.168.43.171/cgi-bin/hadoop.py'/>")
