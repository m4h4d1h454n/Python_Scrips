import psutil
import time
import requests
from datetime import datetime
print("apps on")

while(True):
        battery = psutil.sensors_battery()
        ac = battery.power_plugged
        percent = battery.percent
        spercent = str(percent)
        today = datetime.today()
        time_string = today.strftime("%d-%m-%Y %H:%M:%S")
        
        if ac == False:
                if percent < 30:
                        
                        data = "Hi Boss\n***Personal System Backup Power is critical***\n\nCPU usage: "+str(psutil.cpu_percent(4))+"\nMemory usage: "+str(psutil.virtual_memory()[2])+"\nCurrent Battery: "+spercent+"%\nTime: "+time_string+"\n\nPlease Plug In"
                        r = requests.get('https://api.telegram.org/bot5899518935:AAFAYQ0QoaxtKhiyRFgwfkyILLd-fAFXUvA/sendMessage?chat_id=-703960512&text='+data,
                                headers={'Accept': 'application/json'})
                        
                        print("Critical Alert")


                if percent > 30:
                        
                        data = "Hi Boss\n***Personal System is NOT Pluged In to AC Power***\n\nCPU usage: "+str(psutil.cpu_percent(4))+"\nMemory usage: "+str(psutil.virtual_memory()[2])+"\nCurrent Battery: "+spercent+"%\nTime: "+time_string+"\n\nPlease Plug In"
                        r = requests.get('https://api.telegram.org/bot5899518935:AAFAYQ0QoaxtKhiyRFgwfkyILLd-fAFXUvA/sendMessage?chat_id=-703960512&text='+data,
                                headers={'Accept': 'application/json'})
                        
                        print("OK Alert")
                
        time.sleep(120)
