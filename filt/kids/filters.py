from sys import*
from matplotlib.pyplot import *
from math import *
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages 
from matplotlib import rc
from astropy.io import ascii
from astropy.table import Table, Column, MaskedColumn

rc('text', usetex=True)

clf()
axis([3000, 25000, 0, 1.1])

filt=['u','g','r','i','Z','Y','J','H','Ks']

for i in range(len(filt)):
  catIn=open('KiDSVIKING_aibn139_'+str(filt[i])+'.res','r')
  l,t= np.loadtxt(catIn, dtype='float', usecols=(0,1), unpack=True )
  plot(l,t/(max(t)))

xlabel("lambda")
ylabel("T")
show()
