# !/usr/bin/env python
# -*- coding: utf-8 -*-


import psutil
import sys
import os
import time

while True:
    time.sleep(0.1)
    os.system('cls')

    sys.stdout.write("CPU core num is {0}.\n".format(psutil.cpu_count(logical=False)))
    
    sys.stdout.write("CPU used:" + (str)(psutil.cpu_percent(0)) + "%\n")

    sys.stdout.write("CPU run time:{0}.".format(psutil.cpu_times()))
    

    sys.stdout.write("\n")
    sys.stdout.write("system memory:\n")
    sys.stdout.write("total:{0:.2f}MB.\n".format(psutil.virtual_memory().total / 1024 / 1024))
    sys.stdout.write("available:{0:.2f}MB({1:.1f}%).\n".format(psutil.virtual_memory().available / 1024 / 1024, 100-psutil.virtual_memory().percent))
    sys.stdout.write("used:{0:.2f}MB({1:.1f}%).\n".format(psutil.virtual_memory().used / 1024 / 1024, psutil.virtual_memory().percent))
    

    sys.stdout.write("\n")
    sys.stdout.write("swap memory:\n")
    sys.stdout.write("total:{0:.2f}MB\nused:{1:.2f}MB({2:.1f}%)\nfree:{3:.2f}MB({4:.1f}%)\n".format(psutil.swap_memory().total / 1024 / 1024, psutil.swap_memory().used / 1024 / 1024, psutil.swap_memory().percent, psutil.swap_memory().free / 1024 / 1024, 100 - psutil.swap_memory().percent))
    
    sys.stdout.flush()
