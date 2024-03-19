from sys import*
from matplotlib.pyplot import *
from math import *
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages 
from matplotlib import rc
from astropy.io import ascii
from astropy.table import Table, Column, MaskedColumn

rc('text', usetex=True)



# All the figures will be collected in a single pdf file 
#pdfOut = PdfPages('figures.pdf')

lambda_min=7500
lambda_max=41200
resolution=41.5

flmin=lambda_min
i=0
while flmin < lambda_max :
   fileName='spherex'+str(i)+'.txt'
   fldelta= flmin/(resolution-0.5)
   flmax=flmin+fldelta
   lambd=[flmin-1,flmin,(flmin+flmax)/2.,flmax,flmax+1]
   trans=[0.,1.,1.,1.,0.]
   data = Table([lambd, trans], names=['lambda', 'transmission'])
   ascii.write(data,fileName)
   flmin=flmax
   i=i+1

print 'end'
