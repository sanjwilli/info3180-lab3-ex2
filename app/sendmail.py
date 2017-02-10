import smtplib

#from_addr = 'williamsanjay123@gmail.com'

#to_addr = 'williamsanjay12@gmail.com'

#message = """From: {from_name} <{from_addr}>

To: {to_name} <{to_addr}>

Subject: {subject}

{msg}

"""

message_to_send = message.format(from_name, from_addr, to_name, to_addr, subject, msg)

# Credentails (if needed)

username = 'williamsanjay123@gmail.com'

password = 'dljlcgflwzsrofzd'

# The actual mail send

server = smtplib.SMTP('smtp.gmail.com',587)

server.ehlo()

server.starttls()

server.login(username, password)

server.sendmail(from_addr, to_addr, message_to_send)

server.quit()

# dljlcgflwzsrofzd 