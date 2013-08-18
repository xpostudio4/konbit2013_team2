import schedule 
import time
import gammu
import sys
import smtplib
from fabric.api import local, settings, abort, run, cd
from commands import getstatusoutput
from validate_email import validate_email

#configure mail for sending mail with gmail
fromaddr = 'fromuser@gmail.com'  

# Credentials (if needed)  
username = 'username'  
password = 'password'  

def get_gammu_sms():
	"""The purpose of this function is to connect to the cellphone and get all the sms's and sent them to an url, also the message must be printed on the screen"""
	print "Running Command: Gammu Indetify..."
	
	#initialize the gammu object	
	sm = gammu.StateMachine()
	
	# Read the configuration (~/.gammurc or from command line)
	if len(sys.argv) >= 2:
		sm.ReadConfig(Filename = sys.argv[1])
		del sys.argv[1]
	else:
		sm.ReadConfig()

	#Connect to the phone
	sm.Init()
	#check all the messages in the phone
	#check the amount of folders
	
	#select first inbox to see if there's a message
	try:
		old_sms 					   = sm.GetNextSMS(0,True)
		#get all the info of the message
		from_number, to_number,message = get_message_info(old_sms)
		sms_list   					   = [id(old_sms)]

		while True:
			new_sms = sm.GetNextSMS(0, True)
			if id(new_sms) in sms_list: 
				break
			sms_list.append(id(new_sms))
							
			#process them 
			from_number, to_number,message = get_message_info(new_sms)
	
			#if an email, send it as an email
			to_number =  "".join(to_number.split("#")[0].split(" "))
			try:
				#needs to verify the numbers in the beginning are together
				#If the item is integer validate it has 8 digits
				#verify if the number has 8 digits
				if int(to_number) and (len(str(int(to_number)))==8):
					#make the voice call
					call_number(to_number)
				elif:
					if validate_email(to_number):
					#sends an email
					send_gmail("ljimenez@stancedata.com", to_number, message)
					
					else:
						#send a call to the person telling them is wrong
						call_number(from_number)
						#add the rest of the voice functionality
							
	except Exception:
		print "No new messages"
	#if you want to delete a sms you use "deletesms" and if you want to delete all sms you use "deleteallsms"
schedule.every().minute.do(get_gammu_sms)

while True:
    schedule.run_pending()
    time.sleep(1)

def send_gmail(from_address, to_address,msg):
	server = smtplib.SMTP('smtp.gmail.com:587')  
	server.starttls()  
	server.login(username,password)  
	server.sendmail(fromaddr, toaddrs, msg)  
	server.quit()  

def call_number(phone_number):
	"""Initialize object with a phone_number and call it"""
	sm = gammu.StateMachine()
	
	# Read the configuration (~/.gammurc or from command line)
	if len(sys.argv) >= 2:
		sm.ReadConfig(Filename = sys.argv[1])
		del sys.argv[1]
	else:
		sm.ReadConfig()

	# Connect to the phone
	sm.Init()

	# Dial a number
	sm.DialVoice(phone_number)

def get_message_info(sms):
	text 		= sms[0]['Text']
	from_number = sms[0]['SMSC']['Number']	
	to_number   = text.split('#')[0]
	message 	= "".join(text.split('#')[1:])
	return from_number, to_number, message
