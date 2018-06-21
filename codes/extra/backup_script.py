#!/usr/bin/python3

###################################
#            for Linux            #
###################################
import os
import time

source_dir = ['/root/data']
target_dir = '/root/backup'
today_log_dir = target_dir + os.sep + time.strftime('%y%m%d')
success_count = 0
fail_count = 0
if not os.path.exists(today_log_dir):
    os.makedirs(today_log_dir)

for path in source_dir:
    if not os.path.exists(path):
        print('{0} does not exist'.format(path))
        continue
    else:
        tmp = path.split('/')
        backup_file = today_log_dir + os.sep + tmp[len(tmp) - 1] + '_' + time.strftime('%H%M%S') + '.tar.gz'
        cmd = 'tar -zcPf ' + backup_file + ' ' + path
        if os.system(cmd) == 0:
            print('%r done' % cmd)
            success_count = success_count + 1
        else:
            print('%r failed' % cmd)
            fail_count = fail_count + 1
print('backup:{0} have done.{1} succeeded,{2} failed.'.format(len(source_dir),success_count,fail_count))
