def check_file(sys_args):
        import sys
        from os.path import isfile

        if len(sys_args) == 2:    
            filename = sys_args[1]
            if isfile(filename):
                msg = "Loading configuration parameters from {}"
                print(msg.format(filename) )
            else:
                print("Input argument is not a valid file")
                raise SystemExit(1) 
                
        else:
            print('Configuration file expected (just 1 argument)')
            print('example:  python run_correlation.py ../set/config.ini')
            raise SystemExit(1) 
        
        return filename



def load_parameters(config):
    #{{{
    '''
    Parse paramenters for the simulation from a .ini file
    '''

    from collections import namedtuple
    from astropy import units as u
    import numpy as np

    units = u.Unit(config['exp']['unit'])

    x = (config['exp']['nran']).split('**')

    nran = 1.
    if 'x' in x: 
        s=x.split('x')
        nran = float(s[0])
    for ss in s:
        if '**' in ss:
            p = ss.split('**')
            nran = nran*pow(float(p[0]), float(p[1]))

    smin = float(config['exp']['scale_min'])
    smax = float(config['exp']['scale_max'])
    sbin = int(config['exp']['scale_nbins'])
    nr = np.linspace(start=smin, stop=smax, num=sbin, endpoint=True)
    rh_type = config['exp']['experiment']

    if rh_type in 'CCVT.ccvt.Ccvt': rh_type='ccvt'
    if rh_type in 'GLASS.glass.Glass': rh_type='glass'
    if rh_type in 'ZELREC.ZelRec.zelrec.zel_rec.Zel_Rec.ZEL_REC': \
                   rh_type='zelrec'
    if rh_type in 'RANCROSS.RanCross.rancross.Ran_Cross.\
                   ran_cross': rh_type='rancross'
    if rh_type in 'RANCROSS.RanSplit.ransplit.Ran_Split.\
                   ran_split': rh_type='ransplit'

    input_dir =  config['dirs']['dir_data'] + config['dirs']['base_in'] +\
                 rh_type + '/'    
    nfiles_max = int(config['exp']['nfiles_max'])


    names = 'units nran smin smax sbin nr rh_type input_dir nfiles_max'
    parset = namedtuple('pars', names)

    res = parset(units, nran, smin, smax, sbin, nr, rh_type, \
            input_dir, nfiles_max)

    return(res)

    #}}}                
 
                                                                 

def test_r_len(fname, nr):
    count = 0.
    with open(fname, 'r') as f:
        for line in f:
            count += 1.
    assert(len(nr) == count)


