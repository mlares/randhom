
# procedure for testing:
# go to root directory and run $ pip install -e .
# go to tst/ and run pytest


import pytest
import numpy as np
import randhom as rh

def test_load_config_1():
    #{{{
    sys_args = ['python','../sets/config.ini']
    filename = rh.check_file(sys_args)
    assert isinstance(filename, str)

def test_load_config_2():
    #{{{
    sys_args = ['../sets/config_small.ini']
    with pytest.raises(SystemExit):
        rh.check_file(sys_args)
 
def test_load_config_3():
    #{{{
    sys_args = ['../sets/nonexistentfile.ini']
    with pytest.raises(SystemExit):
        rh.check_file(sys_args)

