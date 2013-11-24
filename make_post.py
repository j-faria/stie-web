#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import sys, os, glob
import re
from datetime import datetime


title = raw_input("Tittle: ")
dateIn = raw_input("Date (y-m-d hh:mm) : ") 
print
content = raw_input("Text: ")

if dateIn in ['today', 'Today', 'now']: 
    now = datetime.now()
    date = '%d-%d-%d %d:%d' % (now.year, now.month, now.day, now.hour, now.minute)
    
last_article = int(glob.glob('content/article*')[0][-5])
print last_article
newfile = 'content/article' + str(last_article+1) + '.rst'
print newfile


#match = re.search(':link:([^\s]+)', content)
#if match:
#    print match.group(0)
#    print re.findall(':\w*', match.group(0))[1]
#    
#    
#print re.sub(':link:([^\s]+)', '<<A LINK!!>>', content)

#External hyperlinks, like `Python
#<http://www.python.org/>`_.

with open(newfile, 'w') as f:
    f.write(title + '\n')
    f.write(len(title)*'#' + '\n\n')
    f.write(':date: ' + date + '\n')
    f.write(':author: João Faria' + '\n\n')
    f.write(content)
    
