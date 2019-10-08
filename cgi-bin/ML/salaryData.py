#!/usr/bin/python3.6

print("content-type: text/html")
print()

import cgi
import numpy
from sklearn.externals import joblib

mydata = cgi.FieldStorage()


file = 'salary.sav'
print("<form action='http://192.168.43.171/cgi-bin/ML/salaryResult.py'>")
print("<input type='text' placeholder='Enter YOF : ' name='expe'/>")

print("<input type='submit' value='Submit' />")
print("</form>")



	
	
