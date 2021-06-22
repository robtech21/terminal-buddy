#!/usr/bin/python3

import os, sys, json
import sys
sys.path.insert(1, 'commands')
from commands import alarm_notifier, news, package_manager, pcinfo, weather, yt_dl

version = 0.1

print(f"TERMINAL BUDDY v{version}")

while(True):
    #Default
    if(len(sys.argv) == 1):
        print("Hey friend, you need to pass an argument to execute a command!")
        sys.exit(0)
    #News command
    elif(sys.argv[1] == "news"):
        print("Getting some news...")
        commands.news.get_news()
        break
    #Cpu temperature command
    elif(sys.argv[1] =="cpu_temp"):
        print("Getting the cpu temperature and info...")
        print(commands.pcinfo.get_cpu_temp())
        break
    #Execute program command
    elif(sys.argv[1] == "exec"):
        print("Executting your command...")
        os.system(sys.argv[2])
        break
    #Disk usage command
    elif(sys.argv[1] == "disk_usage"):
        print("Getting the disk usage and info...")
        print(commands.pcinfo.get_disk_usage())
        break
    #Set alarm commad
    elif(sys.argv[1] == "set_alarm"):
        commands.alarm_notifier.check_alarm()
    #Get weather command
    elif(sys.argv[1] == "weather"):
       commands.weather.get_weather()
       break
    elif(sys.argv[1] == "install"):
        commands.package_manager.install(sys.argv[2])
        break
    elif(sys.argv[1] == "remove"):
        commands.package_manager.remove(sys.argv[2])
        break
    elif(sys.argv[1] == "update"):
        commands.package_manager.update()
        break
    elif(sys.argv[1] == "upgrade"):
        commands.package_manager.upgrade()
        break
    elif(sys.argv[1] == "search"):
        commands.package_manager.search(sys.argv[2])
    elif(sys.argv[1] == "yt_dl"):
        commands.yt_dl.get_video(sys.argv[2])
        break
    #Error
    else:
        print("Hey friend, I don't understand you")
        break
        
