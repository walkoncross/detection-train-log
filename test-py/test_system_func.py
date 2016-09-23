#!/usr/bin/env python

import os

import sys
sys.path.append('/root/workspace/caffe/python')

print  'sys.modules before import caffe: '
print sys.modules
fp = open('sys_modules_before_import_caffe.txt', 'w+')
fp.write(str(sys.modules))
fp.close()

import caffe
print '\nsys.modules after import caffe: '
print sys.modules

fp = open('sys_modulels_after_import_caffe.txt', 'w+')
fp.write(str(sys.modules))
fp.close()
#os.system('ls -l')
