import numpy as np
from astropy.table import Table
from astropy.io import ascii
from astropy import units as u
from sys import argv
import sys

import randhom as rh

#___________________________________
# Load settings

from configparser import ConfigParser
filename = rh.check_file(argv)
config = ConfigParser()
config.read(filename)

#___________________________________
# Prepare experiment


p = rh.load_parameters(config._sections)

from os import listdir
xi_files = listdir(p.input_dir)
rh.test_r_len(p.input_dir + xi_files[0], p.nr)


#___________________________________
# compute

xi0_rs, xi2_rs, xi4_rs = [], [], []

for xi_file in xi_files[:p.nfiles_max]:

    cnames=['xi_0','xi_2','xi_4','xi_6']
    xil_rs = ascii.read(p.input_dir + xi_file,names=cnames)

    xi0_rs.append( xil_rs['xi_0'].data )
    xi2_rs.append( xil_rs['xi_2'].data )
    xi4_rs.append( xil_rs['xi_4'].data )

mean_xi0_rs = np.mean(xi0_rs, axis=0)
mean_xi2_rs = np.mean(xi2_rs, axis=0)
mean_xi4_rs = np.mean(xi4_rs, axis=0)

sd_xi0_rs = np.sqrt(np.var(xi0_rs, axis=0, ddof=1))
sd_xi2_rs = np.sqrt(np.var(xi2_rs, axis=0, ddof=1))
sd_xi4_rs = np.sqrt(np.var(xi4_rs, axis=0, ddof=1))


#________________________________
# write results

cnames = ['xi0', 'xi2','xi4','r']

means = Table([mean_xi0_rs,mean_xi2_rs,mean_xi4_rs,p.nr], names=cnames)
fname = '../data/out/xi_mean/std_c_{}.txt'.format(p.nran)
ascii.write(means, fname, overwrite=True)
 
sds = Table([sd_xi0_rs,sd_xi2_rs,sd_xi4_rs,p.nr], names=cnames)
fname = '../data/out/xi_sd/std_c_{}.txt'.format(p.nran)
ascii.write(sds, fname, overwrite=True)
 
