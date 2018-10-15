from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import base64

def create_msg(subject, html_file):
    message = MIMEMultipart('alternative')
    message['subject'] = subject
    html = open(html_file, 'r').read()%base64.b64encode(open('python.jpeg','rb').read()).decode('utf-8')
    message.attach(MIMEText(html, 'html'))
    return message.as_string()

message = create_msg('Sample Mail', 'mail_body.html')
