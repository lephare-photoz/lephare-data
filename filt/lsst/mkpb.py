import numpy as np
import os
filtList = ['total_g.dat','total_i.dat','total_r.dat','total_u.dat','total_y3.dat','total_y4.dat','total_z.dat']
minList = [350, 600, 450, 300, 900, 850, 750]
maxList = [600, 900, 750, 450, 1150, 1150, 1050]
for i in range(len(filtList)):
    filter = np.loadtxt(filtList[i]).T
    min = (minList[i])
    max = (maxList[i])
    w = np.arange(min, max, step=0.5)
    t = np.interp(w, filter[0], filter[1])
    np.savetxt(filtList[i].replace('.dat','.pb'), np.asarray([10*w, t]).T, fmt="%5i %1.6f")

