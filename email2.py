import os
import smtplib

EMAIL = 'mtabishk200@gmail.com'
PASSWORD = 'testing@123'

sender = EMAIL
reciever = 'mtabishkhanday@gmail.com'
passwd = PASSWORD

server = smtplib.SMTP('smtp.gmail.com',587)
# Encrypts our traffic
server.starttls()
server.login(sender,passwd)
# Enter message that you want to send
message = 'Congratulations Developer--> You achieved your accuracy'
# Sends email
server.sendmail(sender,reciever,message)
# print send message
print("Email send successfully")