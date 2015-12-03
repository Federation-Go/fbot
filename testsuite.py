import json
import argparse
import os
import os.path
from handler import testcase
import sys
import glob

path=os.path.dirname(os.path.realpath(__file__))
os.chdir(path)

def main(*args,**kwargs):
    conf=json.load(open("config/config.json",'r'))
    test_dir=getattr(conf,'test_dir',"testcases")
    testcases=glob.glob("%s/*.test"%test_dir)
    for i in testcases:
        handler=testcase.Testcase(conf['pandora'],i)
        print handler.run_test()

    

if __name__=="__main__":
    main()
