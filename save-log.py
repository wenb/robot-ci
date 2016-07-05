# coding = utf-8

import datetime
from subprocess import *
import os

time_format = '%Y-%m-%d-%H%M'
now = datetime.datetime.now()
log_list = ['output.xml', 'log.html', 'report.html']
str_now = str(now.strftime(time_format))


def rename_move(filename, time, dst_path):

    list_filename = filename.split('.')
    new_filename = list_filename[0]+time+'.'+list_filename[1]

    kwargs = {'shell': True, 'stdout': PIPE, 'stdin': PIPE, 'stderr': PIPE}

    if os.path.exists(filename):
        proc = Popen(
            ['rename', filename,  new_filename, '&&', 'move', new_filename, dst_path],
            **kwargs
        )
        out, error = proc.communicate()
        if error is not None:
            print error

for i in log_list:
    rename_move(i, str_now, 'D:\\')
