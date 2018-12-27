def sendMessage(toNumber='+91xxxxxxxxxx', msgbody="This is a test message.", account_sid = 'xxxxx', auth_token = 'xxxxx', fromNum='+1xxxxxxxxxx'):
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
