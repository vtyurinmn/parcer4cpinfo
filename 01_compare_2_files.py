#
# Взять 2 файла и сравнить их построчно
# 
#

# source files dir:
cpinfo_files = 'C:\\Python\\tmp\\CheckPoint\\files\\Shrinked\\'

# source files:
srcfile1 = 'cpinfo.sc.20160927.info'
srcfile2 = 'cpinfo.sc.20160927_Shrinkage.info'
# or input:
# srcfile = input('Input filename: ')

import os.path
import re
import progressbar
from time import localtime, strftime


def parser(inf1, inf2, outf):
    maxval=100 # Status Bar Max Value
    bar = progressbar.ProgressBar(maxval, \
    widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
    bar.start()
    with open(inf1,'rb') as r1, open(inf2,'rb') as r2, open(outf,'w',encoding='utf-8') as w:
        rBytes = 0 # Bytes Readed form File
        tp = 0 # total progress per 10%
        for line in r1:
            lSize = len(line)
            rBytes = rBytes + lSize
            tp = int(rBytes / size * 100)
            bar.update(tp)
    bar.finish() 
    print("Total " + str(cLines) + " lines.")
    print("Total " + str(cHeaders) + " headers.")
    print('Done!')

# current datetime (for suffix)
datetime=strftime("%Y%m%d_%H%M%S", localtime())

# DIRs
basedir = 'C:\\Python\\tmp\\CheckPoint\\parcer4cpinfo\\'
tmpdir = basedir + 'tmp\\'

# Filenames
infile1 = os.path.abspath(cpinfo_files + srcfile1)
infile2 = os.path.abspath(cpinfo_files + srcfile2)
outfile = os.path.abspath(tmpdir + srcfile1 + '_diff_' + datetime + '.info')

size = os.path.getsize(infile1)
size_gb = round(size/(1024**3),3)
print("Filesize: " + str(size_gb) + " Gb")
print("Outfile: " + str(outfile))

################
#
#   Parser
#
################

parser(infile1, infile2, outfile)