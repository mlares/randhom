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
 
                                                                 

def test_r_len(fname, nr):
    count = 0.
    with open(fname, 'r') as f:
        for line in f:
            count += 1.
    assert(len(nr) == count)


