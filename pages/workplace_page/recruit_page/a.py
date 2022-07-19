import os
from os.path import split

import pytest


def test_xyz( ):
    x=os.path.abspath(os.path.join(os.getcwd(),'../../../../../selenium-compass-remote/script'))+'/正常报备测试数据{0}条.xlsx'
    script_path = os.path.abspath(os.path.join(os.getcwd(), '../../../script//'))+'/正常报备测试数据{0}条.xlsx'
    print(x)
    print(script_path)