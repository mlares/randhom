import glob 
import numpy as np
from astropy.io import ascii
from astropy import units as u
import scipy
from astropy.table import Table
import randhom as rh
import sys
from os import listdir

#___________________________________
# Load settings

from configparser import ConfigParser
#filename = rh.check_file(sys.argv)
filename = rh.check_file([' ','../sets/config.ini'])
config = ConfigParser()
config.read(filename)

#___________________________________
# Prepare experiment

exec('u=u.' + config['exp']['unit'])
exec('nran=' + config['exp']['nran'])

smin = float(config['exp']['scale_min'])
smax = float(config['exp']['scale_max'])
sbin = float(config['exp']['scale_nbins'])
nr = np.linspace(start=smin, stop=smax, num=sbin, endpoint=True)

rh_type = config['exp']['experiment']

if rh_type in 'CCVT.ccvt.Ccvt': rh_type='CCVT'
if rh_type in 'GLASS.glass.Glass': rh_type='GLASS'
if rh_type in 'ZELREC.ZelRec.zelrec.zel_rec.Zel_Rec.ZEL_REC': rh_type='ZELREC'
if rh_type in 'RANCROSS.RanCross.rancross.Ran_Cross.\
               ran_cross': rh_type='RANCROSS'
if rh_type in 'RANCROSS.RanSplit.ransplit.Ran_Split.\
               ran_split': rh_type='RANSPLIT'


input_dir =  config['dirs']['dir_data'] + config['dirs']['base_in'] +\
             rh_type + '/'
xi_files = listdir(input_dir)

rh.test_r_len(input_dir + xi_files[0], nr)

nfiles_max = int(config['exp']['nfiles_max'])
print(nfiles_max)

for xi_file in xi_files[:nfiles_max]:

    xi0_rs, xi2_rs, xi4_rs = [], [], []

    cnames=['xi_0','xi_2','xi_4','xi_6']
    xil_rs = ascii.read(input_dir + xi_file,names=cnames)

    xi0_rs.append( xil_rs['xi_0'].data )
    xi2_rs.append( xil_rs['xi_2'].data )
    xi4_rs.append( xil_rs['xi_4'].data )

mean_xi0_rs = np.mean(xi0_rs, 0)
mean_xi2_rs = np.mean(xi2_rs, 0)
mean_xi4_rs = np.mean(xi4_rs, 0)

mean_rs = Table([mean_xi0_rs,mean_xi2_rs,mean_xi4_rs,nr], \
                names=('xi0', 'xi2','xi4','r'))


#fname_rs =  config['dirs']['dir_data'] + config['dirs']['base_in'] +\
#             rh_type
#
#fname_rs = '../../data/out/mean_xi/' + \
#        config['output']['mean_dir'] + \
#        'mean_rs_{}.txt'.format(nran)
#ascii.write(mean_rs, fname_rs, overwrite=True)
#

#    #Calculate Standard Deviation  
#    mean_xi0_rs = []
#    mean_xi2_rs = []	
#    mean_xi4_rs = []		
#    for ir in range(len(nr)):
#        mean_xi0_rs.append( np.mean([item[ir] for item in xi0_rs]) )
#        mean_xi2_rs.append( np.mean([item[ir] for item in xi2_rs]) )
#        mean_xi4_rs.append( np.mean([item[ir] for item in xi4_rs]) )
#
#    mean_rs = Table([mean_xi0_rs,mean_xi2_rs,mean_xi4_rs,nr], names=('xi0', 'xi2','xi4','r'))
#
#    fname_rs = '../../data/out/mean_xi/mean_rs_{}.txt'.format(Nran)
#    ascii.write(mean_rs, fname_rs, overwrite=True)
#    print('Created {}'.format(fname_rs))
#

