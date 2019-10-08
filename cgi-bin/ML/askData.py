#!/usr/bin/python3.6

print("content-type: text/html")
print()

import cgi
import numpy
from sklearn.externals import joblib

mydata = cgi.FieldStorage()
modelName = mydata.getvalue('model')

print("<b>Enter your R&D expenditure and Administration expenditure </b>")
print("<br>")

#if 'startup' in modelName:

file = 'startup.sav'
#model = joblib.load(file)
print("<form action='http://192.168.43.171/cgi-bin/ML/startup_result.py'>")
print("<input type='text' placeholder='Enter RND Spend : ' name='rnd'/>")

print("<input type='text' placeholder='Enter Administration Spend : ' name='admin'/>")

print("<input type='submit' value='Submit' />")
print("</form>")



	
	
