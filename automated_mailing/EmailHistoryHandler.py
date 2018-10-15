
import sqlite3
import config
from datetime import datetime
import pytz

SUCCESS_STATUS = 1
FAILURE_STATUS = 0
# HAS_ALREADY_SENT = 'SELECT sender, receiver, content  FROM %s WHERE sender="%s" AND receiver="%s" AND content="%s" AND status=%s'
HAS_ALREADY_SENT = 'SELECT sender, receiver, content  FROM %s WHERE receiver="%s" AND status=%s'
INSERT_TO_HISTORY = "INSERT INTO %s (sender, receiver, content, time_stamp, status) VALUES ('%s', '%s', '%s', %s, %s)"
UPDATE_STATUS ='UPDATE %s SET status=%s, time_stamp=%s WHERE sender="%s" AND receiver="%s" AND content="%s"'


class EmailHistoryHandler:
    def __init__(self,sender_email, receiver_email, email_content):
        self.sender_email = sender_email
        self.receiver_email = receiver_email
        self.email_content = str(email_content)

    def has_already_sent_successfully(self):
        """
        Checks if the reciever has status 1 recorded on DB
        """
        connection = sqlite3.connect(config.db_name)
        # fetch_record =connection.execute(HAS_ALREADY_SENT   % (config.email_success_failure_database, self.sender_email,
        #                                                        self.receiver_email, self.email_content, SUCCESS_STATUS))
        fetch_record =connection.execute(HAS_ALREADY_SENT   % (config.email_success_failure_database,
                                                               self.receiver_email, SUCCESS_STATUS))
        records = fetch_record.fetchall()
        connection.close()
        if records:
            return True
        return False

    def has_already_sent_but_failed(self):
        connection = sqlite3.connect(config.db_name)
        # fetch_record = connection.execute(HAS_ALREADY_SENT % (config.email_success_failure_database, self.sender_email,
        #                                                       self.receiver_email, self.email_content, FAILURE_STATUS))
        fetch_record = connection.execute(HAS_ALREADY_SENT % (config.email_success_failure_database,
                                                              self.receiver_email, FAILURE_STATUS))
        records = fetch_record.fetchall()
        connection.close()
        if records:
            return True
        return False

    def add_to_email_history(self, was_sent_successfully = True):
        curr_time = int(datetime.now().replace(tzinfo=pytz.utc).timestamp())
        if(self.has_already_sent_successfully()):
            print("Email has been already sent successfully")
            return
        if(self.has_already_sent_but_failed() and was_sent_successfully):
            connection = sqlite3.connect(config.db_name)
            connection.execute(UPDATE_STATUS %(config.email_success_failure_database,
                                               SUCCESS_STATUS, curr_time, self.sender_email,
                                                self.receiver_email, self.email_content))

            connection.commit()
            return
        if(self.has_already_sent_but_failed() and not was_sent_successfully):
            return

        connection = sqlite3.connect(config.db_name)
        status = FAILURE_STATUS
        if was_sent_successfully:
            status = SUCCESS_STATUS
        connection.execute(INSERT_TO_HISTORY % (config.email_success_failure_database, self.sender_email, self.receiver_email,
                                                self.email_content[:10], curr_time, status))

        connection.commit()
        return True
