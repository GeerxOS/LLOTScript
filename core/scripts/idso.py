#!/usr/bin/python3
#coding: utf-8
import re, sys, subprocess

def gttl(ip_address):
    proc = subprocess.Popen(["/usr/bin/ping -c 1 %s" % ip_address, ""], stdout=subprocess.PIPE, shell=True)
    (out,err) = proc.communicate()
    out = out.split()
    out = out[12].decode('utf-8')
    ttl_value = re.findall(r"\d{1,3}", out)[0]
    return ttl_value

def os(ttl):
    ttl = int(ttl)
    if ttl >= 0 and ttl <= 64:
        return "Linux machine"
    elif ttl >= 65 and ttl <= 128:
        return "Windows machine"
    else:
        return "Not Found machine"

if __name__ == '__main__':
    ip_address = sys.argv[1]
    ttl = gttl(ip_address)
    os_name = os(ttl)
    print("%s (ttl -> %s): %s" % (ip_address, ttl, os_name))