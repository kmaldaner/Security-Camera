def send_email(name):
	import getpass

	from email.MIMEMultipart import MIMEMultipart
	from email.MIMEText import MIMEText
	from email.MIMEImage import MIMEImage

	strFrom = 'kylacamera@gmail.com'
	strTo = 'kylacamera@gmail.com'

	msgRoot = MIMEMultipart('related')
	msgRoot['Subject'] = 'Someone entered your home at ' + name[:-4]
	msgRoot['From'] = strFrom
	msgRoot['To'] = strTo
	msgRoot.preamble = 'This is a multi-part message in MIME format.'

	msgAlternative = MIMEMultipart('alternative')
	msgRoot.attach(msgAlternative)

	msgText = MIMEText('This is the alternative plain text message.')
	msgAlternative.attach(msgText)

	msgText = MIMEText("I've attached a photo of whoever entered", 'html')
	msgAlternative.attach(msgText)

	fp = open(name, 'rb')
	msgImage = MIMEImage(fp.read())
	fp.close()

	msgImage.add_header('Content-ID', '<image1>')
	msgRoot.attach(msgImage)

	password  =open("../auth.txt",'r').read() 

	import smtplib
	smtp = smtplib.SMTP()
	smtp.connect('smtp.gmail.com',587)
	smtp.starttls()
	smtp.login('kylacamera', password)
	smtp.sendmail(strFrom, strTo, msgRoot.as_string())
	smtp.quit()
