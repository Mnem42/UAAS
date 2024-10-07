import kRPC.krpc_main as krpc
import os

import jsonstuff.prefloader as prefloader
import UI.ui      as ui
import UI.manuals as manuals

import time

loadedprefs=prefloader.load_json_file("configs/main.json",True)

termsize = os.get_terminal_size() 
ips = prefloader.load_ipaddrs(prefloader.load_json_file("../../targets.json",True),True)

ui.draw_hr(termsize.columns)

index=-1 #invalid
while index not in range(1,len(ips["valid_ips"])+1):
    index=int(input("\033[96mChoose a target: \033[0m"))

ui.draw_hr(termsize.columns)
print(" "*int((termsize.columns/2)-9),"\033[1mkRPC server ready\033[0m")
client_process=krpc.start_mthread(ips["valid_ips"][index-1][0])
ui.draw_hr(termsize.columns)

while True:
    cmd=input("\033[1;92m>>>\033[0m ")
    tokens=cmd.split(' ')
    
    if(tokens[0]=="ver"):
        if(len(tokens)==1):
            ui.print_error_col("    Invalid arguments. For help, use --help")  
        elif(tokens[1]=="-uaas"):
            ui.print_info_col("    v0.2.0")
        elif(tokens[1]=="-commandline"):
            ui.print_info_col("    v0.1.0")
        else:
            ui.print_error_col("    Invalid arguments. For help, use --help")
            
    if(tokens[0]=="terminate"):
        if(len(tokens)==1 and loadedprefs["commands"]["default-ncon"]==False):
            confirm=str(ui.input_info("    Are you sure? (y/n)"))
            if(confirm=="y"):
                break
            else:
                ui.print_info_col("    Termination cancelled")
        elif(len(tokens)==1 and loadedprefs["commands"]["default-ncon"]):
            break 
        elif(tokens[1]=="--no-confirm" or tokens[1]=="-ncon"):
            break

    if(tokens[0]=="exit" and loadedprefs["commands"]["enable-alternate-exit"]==True):
        break
    
    if(tokens[0]=="manual"):
        print(manuals.load_manual_json("    ",termsize.columns-5))

    if(tokens[0]=="iplist"):
        print(ips)

client_process.terminate()
time.sleep(3)
print("kRPC client terminated")
ui.draw_hr(termsize.columns)
