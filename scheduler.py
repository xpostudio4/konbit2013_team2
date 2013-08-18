import schedule 
import time
from fabric.api import local, settings, abort, run, cd
from commands import getstatusoutput
def job():
	print('I am working... ')

def get_gammu_sms():
	"""The purpose of this function is to connect to the cellphone and get all the sms's and sent them to an url, also the message must be printed on the screen"""
	print "Running Command: Gammu Indetify..."
	status, text = getstatusoutput('gammu identify')
	
	if text != "26624 Error opening device, it doesn't exist.":
		status, text = getstatusoutput('gammu getallsms')		
		print status, text
	 #if you want to delete a sms you use "deletesms" and if you want to delete all sms you use "deleteallsms"
schedule.every().minute.do(get_gammu_sms)

while True:
    schedule.run_pending()
    time.sleep(1)
