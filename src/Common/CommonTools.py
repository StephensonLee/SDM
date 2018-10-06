#!/usr/bin/env python
#coding: utf-8
'''
Created on Oct 4, 2018

@author: xingtong
'''

import socket
from datetime import datetime
from datetime import timedelta

SO_BINDTODEVICE=25

def get_host_ip():
    '''
    get the host ip
    @return: the host ip
    '''
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
#     ip='localhost'
    return ip

def get_free_port(iface=None):
    #  iface参数指Linux的网卡接口，如(eth0,wlan0)，这个参数只支持Linux并且需要root权限
    s = socket.socket()
    if iface:
        s.setsockopt(socket.SOL_SOCKET, SO_BINDTODEVICE, bytes(iface,'utf8'))
    s.bind(('',0))
    port = s.getsockname()[1]
    s.close()
    return port

def calcuteDatetime(orginDatetime=datetime.now(),minutes=0):
    return orginDatetime + timedelta(minutes=minutes)
    

if __name__=='__main__':
    time1 = datetime.now()
    print 'today is %s' % time1.strftime('%Y-%m-%d %H:%M')
    aDay = timedelta(minutes=1)
    time2 = time1 + aDay
    print time2.strftime('%Y-%m-%d %H:%M')
    print time2>=time1
