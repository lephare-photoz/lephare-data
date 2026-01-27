# Plot (file or window) the observed magnitudes
# of the objects, along with best-fit templates, 
# reading the info form .zsp and .pdz output 
# files of LePhare.

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages 
import sys, getopt
#import subprocess
from lephare._spec import plotspec

######## GET FILENAMES AND OPTIONS ########

nspec=len([s for s in sys.argv if s.find('.spec', -5) >=0 ]) # N of .spec files
odev='screen'  # print on screen as default 
sout='' ## use -o arg. to append a suffix to each file, just before .png/.eps/.ps

options, args=getopt.getopt(sys.argv[nspec+1:],"ho:d:c:",["help","output=","device=","context="])
for opt, arg in options:
    if opt in ('-o','--output'):
        sout=arg       
    if opt in ('-d','--device'): 
        if not (arg in ['pdf','png','eps','ps']):
           print("Please choose one of the following devices for output:")
           print("pdf, png, eps, ps")
           sys.exit()
        odev='.'+arg
        print('output device will be in '+odev+' format.')  #can be png,pdf (if none print on screen)
    if opt in ('-c','--context'): 
        print('context for models: ', arg)
        ctx=arg
    if opt in ('-h','--help'):
        print("""HELP still to be finished!!!
SYNTAX:  python spec.py file[s].spec [OPTIONS]

VARIABLES:
             file[s] must be the output files from LePhare
             (option SPEC_OUT = YES). Suffix .spec is 
             compulsory.
OPTIONS:
        -d --device[=STR]:
             select the output device; 
             the string STR can be 'png','pdf','eps','ps'
             (without quotes). If 'pdf' is chosen, all the plots
             are collected in a single file. 
             If the option is not set, then print on screen (with
             a limit of 1 object/window).
        -o --output[=STR]:
             if --device = pdf, this option specifies the name of 
             the pdf file. With any other --device values, a 
             string STR is appended at the end of the filename,
             just befor the extension (e.g. *STR.png). 
             Do nothing when printing on screen.  
        -c --context: 
             TO BE IMPLEMENTED
        -h --help:
             print this help

        """)
        sys.exit()

if nspec==0:
    print('Please specify at least one .spec file')
    print('Try -h or --help options to get help.' )
    sys.exit()

if odev=='screen' and nspec > 1:
    print ("""
Too many windows to be opened!
please reduce the number of .spec files
to one, or chose another output device.
""")
    sys.exit()

if odev=='.pdf': 
   print("All objects will be collected in a single pdf file named:")
   if len(sout)>0: 
       print("--> ", sout+odev)
       pdp = PdfPages(sout+odev)
   else: 
       print("--> MULTISPEC.pdf")
       pdp = PdfPages('MULTISPEC.pdf')
elif odev!='screen':
   if len(sout)>0:
       odev=sout+odev      
#when print on screen --output arg is not used

####### LOOP OVER .SPEC FILES ########

for k in range(nspec):

  ### Open .spec file[s] and read the parameters
  filename=sys.argv[1+k].replace('.spec','')
  plotspec(filename+'.spec')

  if  odev=='.pdf': 
      plt.savefig(pdp,format='pdf',dpi=300,bbox_inches='tight')
      plt.close()
  elif odev=='screen':
      plt.show()
  else: 
      plt.savefig(filename+odev, bbox_inches='tight',dpi=300)
      plt.close()

if odev=='.pdf':
    pdp.close()
