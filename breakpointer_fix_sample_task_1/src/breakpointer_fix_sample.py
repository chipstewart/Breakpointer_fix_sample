_author__ = 'stewart'
import sys
import argparse
import os
import subprocess
import numpy as np
import pandas as pd

if not (sys.version_info[0] == 2  and sys.version_info[1] in [7]):
    raise "Must use Python 2.7.x"

def parseOptions():
    description = '''
    Parse Breakpointer somatic.details.txt, replace sample with pairOd from 
    '''

    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('-d', '--BP_input_file', metavar='BP_input_file', type=str, help='REBC BP details.txt.')
    parser.add_argument('-i', '--pair_id', metavar='id', type=str, help='sample id.',default='')
    parser.add_argument('-o', '--outdir', metavar='outdir', type=str, help='output area', default='.')
    parser.add_argument('-s', '--STUB', metavar='STUB', type=str, help='output file name stub', default='REBC')

    args = parser.parse_args()

    return args

def cmd_exists(cmd):
    return subprocess.call("type " + cmd, shell=True,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE) == 0


if __name__ == "__main__":

    args = parseOptions()
    pair_id = args.pair_id
    BP_input_file = args.BP_input_file
    outdir = args.outdir
    STUB = args.STUB
    if (len(STUB)>0)&~('.' in STUB):
        STUB='.'+STUB

    if not os.path.exists(outdir):
        os.makedirs(outdir)

    outFile  = outdir +'/'+pair_id+STUB+'.Breakpointer_fix_SV.tsv'
    #outFP_all = file(outFile_all,'wt')

    BP=pd.read_csv(BP_input_file, sep="\t", index_col=None,low_memory=False,dtype=str,compression="infer") #dRangerDetails(BP_input_file)

    if BP.count==0:
        print 'empty file'
        BP.to_csv(outFile, sep="\t", index=None)
        sys.exit(0)

    BP['individual'] = pair_id
#
    BP.to_csv(outFile, sep="\t", index=None)
    print('\ndone')
