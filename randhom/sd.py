import numpy as np
from astropy.table import Table
from astropy.io import ascii
from astropy import units as u
from sys import argv

import randhom as rh

#___________________________________
# Load settings

from configparser import ConfigParser
#filename = rh.check_file(argv)
filename = rh.check_file([' ', '../sets/config.ini'])
config = ConfigParser()
config.read(filename)

#___________________________________
# Prepare experiment

from os import listdir

exec('units=u.' + config['exp']['nran'])
exec('nran=' + config['exp']['nran'])

smin = float(config['exp']['scale_min'])
smax = float(config['exp']['scale_max'])
sbin = float(config['exp']['scale_nbins'])
nr = np.linspace(start=smin, stop=smax, num=sbin, endpoint=True)
rh_type = config['exp']['experiment']

if rh_type in 'CCVT.ccvt.Ccvt': rh_type='CCVT'
if rh_type in 'GLASS.glass.Glass': rh_type='GLASS'
if rh_type in 'ZELREC.ZelRec.zelrec.zel_rec.Zel_Rec.ZEL_REC': \
               rh_type='ZELREC'
if rh_type in 'RANCROSS.RanCross.rancross.Ran_Cross.\
               ran_cross': rh_type='RANCROSS'
if rh_type in 'RANCROSS.RanSplit.ransplit.Ran_Split.\
               ran_split': rh_type='RANSPLIT'

input_dir =  config['dirs']['dir_data'] + config['dirs']['base_in'] +\
             rh_type + '/'
xi_files = listdir(input_dir)
nfiles_max = int(config['exp']['nfiles_max'])
rh.test_r_len(input_dir + xi_files[0], nr)

#___________________________________
# compute

xi0_rs, xi2_rs, xi4_rs = [], [], []

for xi_file in xi_files[:nfiles_max]:

    cnames=['xi_0','xi_2','xi_4','xi_6']
    xil_rs = ascii.read(input_dir + xi_file,names=cnames)

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

means = Table([mean_xi0_rs,mean_xi2_rs,mean_xi4_rs,nr], names=cnames)
fname = '../data/out/xi_mean/std_c_{}.txt'.format(nran)
ascii.write(means, fname, overwrite=True)
 
sds = Table([sd_xi0_rs,sd_xi2_rs,sd_xi4_rs,nr], names=cnames)
fname = '../data/out/xi_sd/std_c_{}.txt'.format(nran)
ascii.write(sds, fname, overwrite=True)
 
