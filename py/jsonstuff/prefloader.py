import json
import ipaddress
import os.path
import re
import subprocess
from ping3 import ping, verbose_ping
from urllib import request

def load_json_file(name,print_status):
    if(not os.path.isfile(name)):
        if(print_status):
            print("✘         File not found");
        raise FileNotFoundError(name+" does not exist");
    if(print_status):
        print("\033[92m✓          File loaded\033[0m")

    data={}
    with open(name) as data:
        try:
            data = json.load(data)
        except ValueError as e:
            if(print_status):
                print("✘          JSON invalid")
            raise ValueError("JSON invalid")
        if(print_status):
            print("\033[92m✓          JSON loaded\033[0m")
    return data;

def load_ipaddrs(data,print_details):
    index=0;
    iptable=[]
    validips=[]
    for i in data['targets']:
        valid=True
        ipexists=True
        conntime=0
        try:
            ipaddress.ip_address(i["ip"])
            # legal
        except ValueError:
            valid=False
            ipexists=False
            # Not legal
            
        try:
            conntime=ping(i["ip"])
            if(conntime>5):
                ipexists=False
                valid=True
        except TypeError:
            ipexists=False
            valid=True

            
        index+=1
        if(valid and ipexists and conntime <= 2):
            validnum=len(validips)+1
            if(print_details):
                print ("    ",str(index).ljust(2),
                       str(validnum).ljust(2),
                       "ip: ", i['ip'].ljust(15),
                       "name: ", i['displayname'])
            iptable +=[[i["ip"],i["displayname"],validnum]]
            validips+=[[i["ip"],i["displayname"],validnum]]
            continue
    
        if(not ipexists and valid):
            if(print_details):
                print("\033[93m⚠ CN\033[0m",str(index).ljust(2),
                      "   ip: ", i['ip'].ljust(15),
                      "name: ", i['displayname'])
            continue
        if(not valid):
            if(print_details):
                print("\033[93m⚠ IP\033[0m",str(index).ljust(2),
                      "   ip: ", i['ip'].ljust(15),
                      "name: ", i['displayname'])
            continue
        if(valid and ipexists and conntime > 2):
            if(print_details):
                print("\033[93m⚠ TM\033[0m",str(index).ljust(2),
                      "   ip: ", i['ip'].ljust(15),
                      "name: ", i['displayname'])
            continue
    if(print_details):
        print("\033[92m✓          Data loaded\033[0m")

    return {"valid_ips":iptable}

def load_checklists():
    pass
        
