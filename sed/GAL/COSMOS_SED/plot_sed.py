import numpy as np
import matplotlib
from matplotlib import pyplot as plt, colors
matplotlib.use('Agg')
from matplotlib.pyplot import *
from matplotlib.backends.backend_pdf import PdfPages 
import sys, getopt
from math import *
from sklearn.linear_model import LinearRegression

          

# Define the output pdf
pdfOut = PdfPages('SED.pdf')

# read the SED list
file_sed=open('COSMOS_MOD.list','r')
name_sed= np.loadtxt(file_sed, dtype='str', usecols=(0), unpack=True )

axis([1000,40000,-5,-1])

# color map limits
norm = colors.Normalize(vmin=0.0, vmax=len(name_sed))

# Look over each SED
for i in range(len(name_sed)):
  print(name_sed[i])
  cmap = cm.copper
  # Read each SED
  sed=open('../'+name_sed[i],'r')
  l,f= np.loadtxt(sed, dtype='float', usecols=(0,1), unpack=True )
  # Plot the SED
  lfin=l
  ffin=f
  plot(lfin,np.log10(ffin),color=cmap(norm(float(i))))

# Labels and titles
xlabel('$\lambda$', fontsize=18, labelpad=13)
ylabel('log(f)', fontsize=18, labelpad=13)
  
# Save the pdf
savefig(pdfOut,format='pdf')
pdfOut.close()


