import os

SSID = "Rezwan khepi"  
PASSWORD = "password123"  

os.system(f'netsh wlan set hostednetwork mode=allow ssid={SSID} key={PASSWORD}')
os.system('netsh wlan start hostednetwork')
