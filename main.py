import os
import time
from datetime import datetime

now = datetime.now()
dateString = now.strftime('%m/%d/%Y %H:%M')



def testConnection():
    os.system('date +%l:%M >> net-log')
    os.system('speedtest-cli >> net-log')    


while True:
    print('Testing Connection...')
    testConnection()
    print('Test completed and logged')
    time.sleep(2)
    f = open('net-log')
    content = f.readlines()
    down = content[-3]
    up = content[-1]
    f.close()
    print(dateString)
    print(down)
    print(up)
    time.sleep(300)