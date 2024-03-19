from sys import*
import matplotlib
matplotlib.use('Agg')
from matplotlib.pyplot import *
from math import *
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages 

rc('text', usetex=True)

catIn=open(sys.argv[1],'r')
lsvo,tsvo= np.loadtxt(catIn, dtype='float', usecols=(0,1), unpack=True)
catIn=open(sys.argv[1],'r')
ljwst,tjwst= np.loadtxt(catIn, dtype='float', usecols=(0,1), unpack=True)

pdfOut = PdfPages('filt.pdf')

#axis([35000,60000,0,0.0015])

plot(lsvo,tsvo/np.sum(tsvo), color='green',alpha=0.5,ls='--')
plot(ljwst,tjwst/np.sum(tjwst), color='red',alpha=0.5)

xlabel('lambda', fontsize=12)
ylabel('T', fontsize=12)

savefig(pdfOut,format='pdf')
pdfOut.close()
