import config
from multiprocessing import Pool
from SenderListHandler import SenderListHandler
from MailHandler import  MailHandler
from InitialSetup import  create_db_and_tables
from CommonUtils import get_domain_from_email
import threading
import pandas as pd
import MailContent

def send_to_all_receivers(mail_handler, receiver_list, message):
    for receiver in receiver_list:
        mail_handler.send_email(receiver = receiver, content = message)


def bulk_send_email(message):
    file_to_read = config.receiver_list_file_name
    receiver_list = [x.strip() for x in open(file_to_read)]
    senderListHandler = SenderListHandler()
    senders_list = senderListHandler.get_senders_list_from_email()
    threads = []
    for sender in senders_list:
        email = sender["email"]
        password = sender["password"]
        smtp_details = senderListHandler.get_smtp_details_for(email)
        smtp_host = smtp_details["smtp_host"]
        smtp_port = smtp_details["smtp_port"]
        mail_handler = MailHandler(email, password, smtp_host, smtp_port)
        t = threading.Thread(target=send_to_all_receivers, args=(mail_handler, receiver_list, message,))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()



if __name__ == '__main__':
    create_db_and_tables()
    senderListHandler = SenderListHandler()
    senders = pd.read_csv(config.sender_file)
    for _, sender in senders.iterrows():
        senderListHandler.insert_sender_email_into_db(sender['email'], sender['password'])
        senderListHandler.insert_smtp_host_detail_into_db(get_domain_from_email(sender['email']), sender['host'], sender['port'])
    message = MailContent.message
    bulk_send_email(message)
