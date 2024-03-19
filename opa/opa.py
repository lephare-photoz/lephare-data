from sys import*
import matplotlib
from matplotlib.pyplot import *
from math import *
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages 

catIn=open('tau10.out','r')
l,t=np.loadtxt(catIn,usecols=(0,1),unpack=True,dtype=float)
plot(l,t)
show()
