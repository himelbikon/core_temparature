import time, subprocess, re
from datetime import datetime

tem_limit = 45

def main():
	output = subprocess.check_output('sensors', shell=True)
	tem_of_core = re.findall('       \W\d\d.0', output.decode())
	for x in tem_of_core:
		deg = int(x[-4:-2])
		if deg > tem_limit:
			#subprocess.call('notify-send "Core Temparature is %d degrees"' % deg, shell=True)
			status = 'Core Temparature is %d degrees' % deg + ' ' + str(datetime.now()) + '\n'
			f = open('CPU Temparature.txt', 'a')
			f.write(status)
			f.close()
			time.sleep(1)
		else:
			time.sleep(1)

print('Cores temparature is checking in every minute')
while True:
	main()