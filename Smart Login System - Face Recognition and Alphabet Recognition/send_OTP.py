import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def workfun(email):
	string = ""

	for i in range(3):

		n = random.randint(87,122)

		if n<97:
			string = string + str(n-87)
		else:
			string = string + str(chr(n))

	#print(string)

	#print(len(string))


	mail_content = string
#The mail addresses and password
	sender_address = '--your email address'
	sender_pass = '--your password'
	receiver_address = email
#Setup the MIME

	message = MIMEMultipart()
	message['From'] = sender_address
	message['To'] = receiver_address
	message['Subject'] = 'Your OTP is here!'   #The subject line
#The body and the attachments for the mail
	message.attach(MIMEText(mail_content, 'plain'))
#Create SMTP session for sending the mail
	session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
	session.starttls() #enable security
	session.login(sender_address, sender_pass) #login with mail_id and password
	text = message.as_string()
	session.sendmail(sender_address, receiver_address, text)
	session.quit()

	print('Mail Sent')

	return string


