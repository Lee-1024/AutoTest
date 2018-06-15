# _*_ coding:utf-8 _*_
__author__ = 'Lee'
import thread
import time


def print_time(threadname,delay):
    count = 0

    while count < 5:
        time.sleep(delay)
        count = count+1
        print "%s:%s" % (threadname, time.ctime(time.time()))

try:
    thread.start_new_thread(print_time, ("Thread-1",2))
    thread.start_new_thread(print_time, ("Thread-2",4))
except:
    print "ERROR"

while 1:
    pass
