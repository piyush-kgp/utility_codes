import sys
NUM = sys.argv[1]
SID = sys.argv[2]
TOK = sys.argv[3]
FRM = sys.argv[4]

def sendMessage(toNumber=NUM, msgbody="This is a test message.", account_sid=SID, auth_token=TOK, fromNum=FRM):
    from twilio.rest import Client
    account_sid = account_sid
    auth_token = auth_token
    client = Client(account_sid, auth_token)
    message = client.messages \
                    .create(
                         body=msgbody,
                         from_=fromNum,
                         to=toNumber
                     )
    print(message.sid)

import subprocess
import platform
bashCommand = 'uptime'
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
output, error = process.communicate()
output = output.decode('utf-8')
msgbody = platform.platform() + output
sendMessage(msgbody=msgbody)
