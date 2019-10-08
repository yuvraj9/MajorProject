#!/usr/bin/python36


print("content-type: text/html")
print()

from sklearn.externals import joblib
import numpy
import cgi
from sklearn.linear_model import LinearRegression


mydata = cgi.FieldStorage()

rnd =int( mydata.getvalue('rnd'))
admin =int( mydata.getvalue('admin'))

X =[[rnd,admin]]
#X= X.numpy.reshape((X.shape[0],1))

file = 'startup.sav'
model=joblib.load(file)
result = model.predict(X)
print("Predicted Profit : {} ".format(result[0]))

