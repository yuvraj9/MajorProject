#!/usr/bin/python36


print("content-type: text/html")
print()

from sklearn.externals import joblib
import numpy
import cgi
from sklearn.linear_model import LinearRegression


mydata = cgi.FieldStorage()

expe =int( mydata.getvalue('expe'))

X =[[expe]]
#X= X.numpy.reshape((X.shape[0],1))

file = 'salary.sav'
model=joblib.load(file)
result = model.predict(X)
print("Expected salary is : {} ".format(result[0]))

