#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 13:04:55 2018

@author: last-chance
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt

mean_x= np.array([1,2])
print mean_x
mean_x_t=np.transpose(mean_x)
print "x transpose"
print mean_x_t

mean_xo= np.array([(1),(2)])
print mean_xo


variance1=1
std_dev1=1
variance2=2
std_dev2=np.float32(np.sqrt(2))
r=np.float32(0.75)
#Normal distribution y with mean 0 and variance Identity matrix
mean_y=0
variance_y=np.identity(2);  #  recheck 
print variance_y


covaraince_coefficient= 1/(1-np.square(r))
covariance_matrix_x_y =np.array([(variance1 , r*std_dev1*std_dev2),(r*std_dev1*std_dev2 , variance2)], dtype='f')
print "covariance matrix"
print covariance_matrix_x_y

print covariance_matrix_x_y[0,0]
print "cholesky factorization"

beta11 = np.sqrt(variance1)
beta12 = 0
beta21 = r*std_dev1*std_dev2/beta11
beta22 = np.sqrt(variance2 - np.square(beta21))

cholesky_matix = np.array([(beta11, beta12),(beta21, beta22)])
print "cholesky_matix"
print cholesky_matix

mean_y= np.array([0,0])
print mean_y
mean_y_t=np.transpose(mean_y)
#set_y1,set_y2 = np.random.multivariate_normal(mean_y_t,variance_y,10).T


sy1=np.random.normal(0,1,100000) 
print "sy1"
#print sy1   
sy2=np.random.normal(0,1,100000)   

print "values of the test set"
#print x[0][1]    

set_x1 =beta11*sy1 + beta12*sy2 + 1
set_x2 =beta21*sy1 + beta22*sy2 + 2
#print set_x1
print set_x2



######## contour plot 
plt.figure()
plt.scatter(set_x1,set_x2)
H, x1edges, x2edges = np.histogram2d(set_x1, set_x2, bins=(50, 50))
H=H.T
x1centers = (x1edges[:-1] + x1edges[1:]) / 2
x2centers = (x2edges[:-1] + x2edges[1:]) / 2
############################# contour plot  #######################
plt.contour(x1centers, x2centers, H)
#plt.title(" plot of the x 2D data")
plt.show()








