#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 23:09:53 2018

@author: VarunGarg
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stat


mean_xo= np.array([(1),(2)])


variance1=1
std_dev1=1
variance2=2
std_dev2=np.float32(np.sqrt(2))

r=np.float32(0.75)



########################cholesky factorization#################

beta11 = np.sqrt(variance1)
beta12 = 0
beta21 = r*std_dev1*std_dev2/beta11
beta22 = np.sqrt(variance2 - np.square(beta21))

cholesky_matix = np.array([(beta11, beta12),(beta21, beta22)])


################################################################
n_bins=100
n_samples= 1000000
sy1=np.random.normal(0,1,n_samples) 
print "sy1"
#print sy1   
sy2=np.random.normal(0,1,n_samples)   

print "values of the test set"
#print x[0][1]    

set_x1 =beta11*sy1 + beta12*sy2 + 1
set_x2 =beta21*sy1 + beta22*sy2 + 2
#print set_x1
print set_x2

print "Variance fx1"
print np.var(set_x1)
print "Variance fx2"
print np.var(set_x2)


################ histogram of fx2

plt.figure()

hist_x2,bins_x2= np.histogram(set_x2, bins =n_bins,density=True)

#####plotting histogram of x2

plt.hist(set_x2,bins=n_bins,density=True)

#### marginal pdf of x2 using the bins

bins_x2_width     =bins_x2[1]-bins_x2[0]
#bins_x2  =bins_x2[0:n_bins] + bins_x2_width/2

bins_x2  =bins_x2[0:n_bins] 

xcalc = stat.norm.pdf(bins_x2, 2, np.sqrt(2))

plt.plot(bins_x2,xcalc)



################ histogram of fx2

plt.figure()

hist_x1,bins_x1= np.histogram(set_x1, bins =n_bins,density=True)

#####plotting histogram of x2

plt.hist(set_x1,bins=n_bins,density=True)

#### marginal pdf of x2 using the bins

bins_x1_width=bins_x1[1]-bins_x1[0]

bins_x1 = bins_x1[0:n_bins] 

xcalc   = stat.norm.pdf(bins_x1, 1, np.sqrt(1))

plt.plot(bins_x1,xcalc)




