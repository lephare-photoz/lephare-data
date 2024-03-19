from sys import*
from matplotlib.pyplot import *
from math import *
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages 
from matplotlib import rc
from astropy.io import ascii
from astropy.table import Table, Column, MaskedColumn

rc('text', usetex=True)

sensIn=open("spherex_sensitivity.dat",'r')
print "Name of the sensitivity file : ",sensIn
sensLamb,sensShallow,sensDeep = np.loadtxt(sensIn, dtype='float', usecols=(0,2,3), unpack=True )


for sens in xrange(len(sensLamb)-1) :
   fileName='spherexNew'+str(sens)+'.txt'
   flmin=sensLamb[sens]*10000.
   flmax=sensLamb[sens+1]*10000.
   lambd=[flmin-1.,flmin,(flmin+flmax)/2.,flmax,flmax+1]
   trans=[0.,1.,1.,1.,0.]
   data = Table([lambd, trans], names=['lambda', 'transmission'])
   ascii.write(data,fileName)

print 'end'
