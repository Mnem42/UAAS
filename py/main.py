import krpc #ignore for now
import prefloader
import ui
import os

termsize = os.get_terminal_size() 
ips = prefloader.load_ipaddrs(prefloader.load_json_file("../../targets.json",True),True)

ui.draw_hr(termsize.columns)

index=-1 #invalid
while index not in range(1,len(ips)+1):
    index=int(input("\033[96mChoose a target: \033[0m"))

ui.draw_hr(termsize.columns)
print(" "*int((termsize.columns/2)-9),"\033[1mkRPC server ready\033[0m")
ui.draw_hr(termsize.columns)

while True:
    cmd=input("\033[1;92m>>>\033[0m ")
    if(cmd=="ver-main"):
        ui.print_info_col("    "+"v0.1.0")
    if(cmd=="exit"):
        break;

ui.draw_hr(termsize.columns)
