import numpy as np
import matplotlib
from matplotlib import pyplot as plt, colors
matplotlib.use('Agg')
from matplotlib.pyplot import *
from matplotlib.backends.backend_pdf import PdfPages 
import sys, getopt
from math import *
from sklearn.linear_model import LinearRegression

def extrapolation(le,fe):
    # last value of tyhe flux
    lastlamb=le[-1]
    lastlgf=np.log10(fe[-1])
    # Create linear regression object
    regr = LinearRegression()
    # Select the positive flux and the last 200A 
    condfl=(le>lastlamb-4000) & (fe>0)
    # Check that they are elements above 0
    if(len(fe[condfl])>2):
      # Do the fit
      regr.fit((le[condfl]).reshape((-1, 1)), np.log10(fe[condfl]))
      # Add lambda over 1000000 angstrom for extrapolation
      for i in range(1,100):
          le=np.append(le,lastlamb+float(i)*10000.)
          fe=np.append(fe,pow(10.,regr.coef_[0]*(le[-1]-lastlamb)+lastlgf))
    else:
          # Add a zero at really long wavelength
          np.append(le,1000000000.)
          np.append(fe,0.)
    return le,fe
          

# Define the output pdf
pdfOut = PdfPages('SED.pdf')

# read the SED list
file_sed=open('AGN_MOD.list','r')
name_sed= np.loadtxt(file_sed, dtype='str', usecols=(0), unpack=True )

axis([00,3000,-5,3])
#axis([20000,30000,-3,3])

# color map limits
norm = colors.Normalize(vmin=0.0, vmax=len(name_sed))

# Look over each SED
for i in range(len(name_sed)):
  print(name_sed[i])
  cmap = cm.copper
  # Read each SED
  sed=open('../'+name_sed[i],'r')
  l,f= np.loadtxt(sed, dtype='float', usecols=(0,1), unpack=True )
  # extrapolation
  #cond=(l<24950)
  #lfin,ffin=extrapolation(l[cond],f[cond])
  # Plot the SED
  #plot(lfin,np.log10(ffin),color=cmap(norm(float(i))))
  plot(l,np.log10(f),color=cmap(norm(float(i))))
  #outf = open('../'+name_sed[i]+'.ext', "w+")
  ## Saving the array in a text file
  #for l in range(len(lfin)):
  #  outf.write(str(lfin[l])+' ' + str(ffin[l]) + '\n')
  #outf.close()

# Labels and titles
xlabel('$\lambda$', fontsize=18, labelpad=13)
ylabel('log(f)', fontsize=18, labelpad=13)
  
# Save the pdf
savefig(pdfOut,format='pdf')
pdfOut.close()


