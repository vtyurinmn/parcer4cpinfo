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


def parser(inf1, inf2, out_sh, out_diff):
    maxval=100 # Status Bar Max Value
    bar = progressbar.ProgressBar(maxval, \
    widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
    bar.start()
    with open(inf1,'rb') as r1, open(inf2,'rb') as r2, open(out_sh,'wb') as w, open(out_diff,'wb') as w_diff:
        rBytes = 0 # Bytes Readed form File
        tp = 0 # total progress per 10%
        cDiffLines = 0 # total different lines
        skip = False # skip read new line while diff
        tmp_i = 0 # temp count
        pause = True # pause parser
        total_lines = 0
        total_equal_lines = 0
        
        for r1line in r1:
            total_lines += 1
            lSize = len(r1line)
            rBytes = rBytes + lSize
            tp = int(rBytes / size * 100)
            bar.update(tp)
            
            r1line_str= str(r1line.decode(encoding='utf-8',errors='replace')).strip() # avoid UnicodeDecodeError
            #print('r1line: ' + r1line_str)
            
            #tmp_i += 1
            #if tmp_i > 100000:
            #    break
            
            if not skip:
                r2line=r2.readline()
                r2line=r2line.decode(encoding='utf-8',errors='replace') # avoid UnicodeDecodeError
                r2line_str=str(r2line) # avoid UnicodeDecodeError
                r2line_str=r2line_str.strip()
                #print('r2line: ' + r2line_str)
                w.write(r1line)
                
            #print(r1line_str.find(r2line_str))
            
            if r1line_str.find(r2line_str) == -1:
                cDiffLines += 1
                w_diff.write(r1line)
                skip = True
                #print('r1line: ' + r1line_str)
                #print('r2line_diff: ' + r2line_str)
                if pause:
                    #input()
                    pause = False
            else:
                total_equal_lines += 1
                skip = False
                pause = True
            
            
    bar.finish() 
    print("Total " + str(total_lines) + " headers.")
    print("Total " + str(total_equal_lines) + " equal lines.")
    print("Total " + str(cDiffLines) + " different lines.")
    print("Check Sum: " + str(cDiffLines + total_equal_lines))
    print('Done!')

# current datetime (for suffix)
datetime=strftime("%Y%m%d_%H%M%S", localtime())

# DIRs
basedir = 'C:\\Python\\tmp\\CheckPoint\\parcer4cpinfo\\'
tmpdir = basedir + 'tmp\\'

# Filenames
infile1 = os.path.abspath(cpinfo_files + srcfile1)
infile2 = os.path.abspath(cpinfo_files + srcfile2)
outfile_shrinked = os.path.abspath(tmpdir + srcfile1 + '_shrinked_' + datetime + '.info')
outfile_diff = os.path.abspath(tmpdir + srcfile1 + '_diff_' + datetime + '.info')

size = os.path.getsize(infile1)
size_gb = round(size/(1024**3),3)
print("Filesize: " + str(size_gb) + " Gb")
print("Outfile 1: " + str(outfile_shrinked))
print("Outfile 2: " + str(outfile_diff))

################
#
#   Parser
#
################

parser(infile1, infile2, outfile_shrinked, outfile_diff)