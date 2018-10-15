
import sqlite3
import config
import datetime
from datetime import datetime
import pytz
from EmailLimitHandler import  EmailLimitHandler
from EmailHistoryHandler import EmailHistoryHandler
from  CommonUtils import  send_email
from CommonUtils import LOGGER_INFO, \
    LOGGER_WARNING, LOGGER_ERROR
from ReceiverHandler import ReceiverHandler
import traceback

from  EmailLimitHandler import  EmailLimitHandler

class MailHandler:

    def __init__(self,email, password, smtp_host, smtp_port):
        self.email = email
        self.password = password
        self.smtp_host = smtp_host
        self.smtp_port = smtp_port


    def send_email(self, receiver, content):
        # print(LOGGER_INFO + ": Email Details:  sender: %s, receiver: %s, content: %s...." %(self.email,receiver,content))
        emailHistoryHandler = EmailHistoryHandler(sender_email=self.email,receiver_email=receiver, email_content=content)
        if emailHistoryHandler.has_already_sent_successfully():
            print("Email has been already sent to the user. Skipping send now")
            return

        receiverHandler = ReceiverHandler(receiver)
        emailLimitHandler = EmailLimitHandler(sender_email=self.email)

        if not emailLimitHandler.is_allowed():
            print("Sender has crossed his/her daily limit. Skipping send now")
            return

        if receiverHandler.is_undeliverable():
            print("Receiver in undeliverable for today. Skipping send now")
            return

        print("Sending email now....")
        try:
            send_email(sender=self.email, password = self.password,receiver=receiver, content=content, smtp_host=self.smtp_host, smtp_port=self.smtp_port)
            emailHistoryHandler.add_to_email_history()
            emailLimitHandler.increment_count()
        except:
            print(LOGGER_ERROR+": Unable to send email...")
            emailHistoryHandler.add_to_email_history(was_sent_successfully=False)
            print(traceback.format_exc())
