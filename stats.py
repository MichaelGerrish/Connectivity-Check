import string
import re
import numpy as np

f = open('net-log')
content = f.readlines()
downSpeedsLine = []
upSpeedsLine = []
downSpeeds = []
upSpeeds = []

for i in content:
    if i.startswith('Down'):
        downSpeedsLine.append(i)
    if i.startswith('Up'):
        upSpeedsLine.append(i)

f.close()

for i in downSpeedsLine:
    result = re.findall(r"[-+]?\d*\.\d+|\d+", i)
    downSpeeds.append(result)

x = np.array(downSpeeds)
downSpeeds = x.astype(float)

##Final Down Average##
downSpeedMean = np.mean(downSpeeds)

for i in upSpeedsLine:
    result = re.findall(r"[-+]?\d*\.\d+|\d+", i)
    upSpeeds.append(result)

y = np.array(upSpeeds)
upSpeeds = y.astype(float)

upSpeedMean = np.mean(upSpeeds)

print(downSpeedMean)
print(upSpeedMean)