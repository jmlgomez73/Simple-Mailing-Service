
# import necessary packages
 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
 
# create message object instance
msg = MIMEMultipart()

x=open("x.py","r")
xy=x.read()


message = "Put here your message" + xy
 
# setup the parameters of the message
password = "xxx"
msg['From'] = "xxx@xxx"
msg['To'] = "xxx@xxx"
msg['Subject'] = "Put here the subject"
 
# add in the message body
msg.attach(MIMEText(message, 'plain'))
 
#create server
server = smtplib.SMTP('smtp.gmail.com: 587')
 
server.starttls()
 
# Login Credentials for sending the mail
server.login(msg['From'], password)
 
 
# send the message via the server.
server.sendmail(msg['From'], msg['To'], msg.as_string())
 
server.quit()
 
print ("successfully sent email to %s:" % (msg['To']))