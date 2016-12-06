#
# Выписать все разделы из файла в отдельный файл
# 
#

# source files dir:
cpinfo_files = 'C:\\Python\\tmp\\CheckPoint\\files\\Shrinked\\'

# source files:
srcfile = 'cpinfo.sc.20160927.info'
#srcfile = 'cpinfo.sc.20160927_Shrinkage.info'
# or input:
# srcfile = input('Input filename: ')

import os.path
import re
import progressbar
from time import localtime, strftime

def parse1(line):
    pattern1 = r'^={46}$'
    pattern2 = r'^-{66}$'
    return re.match(pattern1, line) or re.match(pattern2, line)

def parser(inf, outf):
    maxval=100 # Status Bar Max Value
    bar = progressbar.ProgressBar(maxval, \
    widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
    bar.start()
    with open(inf,'rb') as r, open(outf,'w',encoding='utf-8') as w:
        rBytes = 0 # Bytes Readed form File
        tp = 0 # total progress per 10%
        skip = False # skip read new line while diff
        isPart = False # is partition
        
        total_lines = 0
        total_headers = 0
        
        for line in r:
            total_lines += 1 # count lines
            
            # Update status bar
            lSize = len(line)
            rBytes = rBytes + lSize
            tp = int(rBytes / size * 100)
            bar.update(tp)
            ########
            
            line_str= str(line.decode(encoding='utf-8',errors='replace')).strip() # avoid UnicodeDecodeError
            
            if parse1(line_str):
                isPart = not isPart
                ##continue
            
            if isPart:
                w.write(line_str + '\n')
                total_headers += 1
    bar.finish() 
    print("Total " + str(total_lines) + " lines in file.")
    print("Total " + str(total_headers) + " headers.")
    print('Done!')

# current datetime (for suffix)
datetime=strftime("%Y%m%d_%H%M%S", localtime())

# DIRs
basedir = 'C:\\Python\\tmp\\CheckPoint\\parcer4cpinfo\\'
tmpdir = basedir + 'tmp\\'

# Filenames
infile = os.path.abspath(cpinfo_files + srcfile)
outfile = os.path.abspath(tmpdir + srcfile + '_parts_' + datetime + '.info')

size = os.path.getsize(infile)
size_gb = round(size/(1024**3),3)
print("Filesize: " + str(size_gb) + " Gb")
print("Outfile: " + str(outfile))

################
#
#   Parser
#
################

parser(infile, outfile)