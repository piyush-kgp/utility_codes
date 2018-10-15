import sqlite3
import config
from  CommonUtils import get_today_in_epoch

GET_COUNT_FOR_GIVEN_DATE = 'SELECT sender_email, date_in_epoch, count  FROM %s WHERE sender_email="%s" AND date_in_epoch=%s'
INCREMENT_COUNT_FOR_GIVEN_DATE = "UPDATE %s SET count=%s WHERE sender_email='%s' AND date_in_epoch=%s"
INSERT_COUNT_FOR_GIVEN_DATE="INSERT INTO %s (sender_email, date_in_epoch, count) VALUES ('%s', '%s', %s)"



class EmailLimitHandler:

    def __init__(self, sender_email,date_in_epoch = get_today_in_epoch()):
        self.sender_email = sender_email
        self.limit = config.one_day_limit_for_one_sender
        self.date_in_epoch = date_in_epoch

    def get_count(self):
        connection = sqlite3.connect(config.db_name)
        fetch_record =connection.execute(
            GET_COUNT_FOR_GIVEN_DATE % (
            config.email_timestamp_database_name, self.sender_email, self.date_in_epoch))
        records = fetch_record.fetchall()
        if records:
            return records[0][2]
        connection.close()
        return 0


    def increment_count(self):
        count = self.get_count()
        connection = sqlite3.connect(config.db_name)
        if(count):
            connection.execute(INCREMENT_COUNT_FOR_GIVEN_DATE %(config.email_timestamp_database_name, count+1, self.sender_email, self.date_in_epoch))
            connection.commit()
        else:
            connection.execute(INSERT_COUNT_FOR_GIVEN_DATE % (config.email_timestamp_database_name, self.sender_email, self.date_in_epoch,1))
            connection.commit()
        connection.close()

    def is_allowed(self):
        return self.get_count()<=config.one_day_limit_for_one_sender