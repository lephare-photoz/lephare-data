import numpy as np
from astropy.io import ascii

def ascii2fits(catname,outsuff='',colnames=None):
    """
    Simple script to convert ASCII file to FITS format. 
    An additional string can be appended to the output file name, 
    and column names specified. 
    
    Usage
    -----
    ascii2fits(catname,outsuff='',colnames=None):

    Parameters
    ----------
    catname = name of ASCII file to convert (it is also the name 
              of the output file with additional extention .fits)
    outsuff = additional string to be added between the original
              name and the .fits extension (ie, output file name 
              will be the string catname+outsuff+'.fits')
    colnames = list of strings to be used as column names 
               in the output file (otherwise standard 'col1',
               'col2', etc will be used).
    """
    dat = ascii.read(catname,comment='#',delimiter=' ',guess=False,format='no_header')
    if colnames is not None:  
        # if colnames list is shorter than total number of columns, only the first n-th will change,
        # with n = len(colnames)
        for i,nm in enumerate(colnames): dat.rename_column(dat.colnames[i],nm)
    dat.write(catname+outsuff+'.fits')

def reformat(catname,nbd,cut=(999,99),outsuff='.in'):
    """
    Re-write the photometric catalog used as input in LePhare
    Extremely faint magnitudes, or those with large errors,
    are set equal to -99.
    The CONTEXT column is updated accordingly.
    The output catalog is by default an ASCII file. 
    A smaller version of the output catalog is also saved 
    if `cut` parameter is specified.
    
    Usage
    -----
    reformat(catname,nbd,cut=(999,99),outsuff='.in'):

    Parameters
    ----------
    catname = name of input file to modify
    nbd = number of filters
    cut = list including col number abs(cut[0]) and threshold value cut[1] to make a subselection
          cut[0]<0 means select objects <cut[1], otherwise the selection includes >cut[1] objects 
          NB: this is a column of the output catalog (indexing starts from 0)
    outsuff = the string to append as a suffix to the output file      
    """

    dat = ascii.read(catname,comment='#',delimiter=' ',guess=False,format='no_header')
    outname = catname+outsuff
    cn = dat.colnames
    cut_col = cut[0]; cut_val = cut[1]
    ngal = len(dat)
    # set mag=-99 when outside this range:
    magsatu = [1e-3 for i in range(nbd)]  #brighter limit
    maglim = [30. for i in range(nbd)]    #fainter limit
    # start loop over galaxies
    for i in range(ngal):
        ctx = 0
        for j in range(nbd):
            if dat[cn[j*2+1]][i]<magsatu[j] or dat[cn[j*2+1]][i]>maglim[j]  or dat[cn[j*2+2]][i]>10. or dat[cn[j*2+2]][i]<0.:
                dat[cn[j*2+1]][i]=-99.
                dat[cn[j*2+2]][i]=-99.
            else:
                ctx += 2**j
        dat[cn[j*2+2+1]][i] = ctx
    
    print("Writing output catalog {}".format(outname))
    dat.write(outname,format='ascii.no_header')
    if cut_col<990:
        #only a portion (RA>0.25, roughly a quarter)
        print("... and smaller version {}".format(outname+'.subsel'))
        if cut_col>0.:  dat2 = dat[dat[cn[cut_col]]>cut_val]
        else:  dat2 = dat[dat[cn[-cut_col]]<cut_val]
        dat2.write(outname+'.subsel',format='ascii.no_header')
     
