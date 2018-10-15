import sqlite3
import config
from datetime import datetime
import pytz
GET_COUNT_UNDELIVERED = "select count(*) from %s where status=%s and  time_stamp between %s and %s"
FAILED_STATUS = 0

class ReceiverHandler:
    def __init__(self, email):
        self.email = email

    def is_undeliverable(self):
        """
        Checks for the number of undelivered mails sent in last 24 hours rom DB
        and checks if it is greater than undeliverable_count
        """
        curr_time = int(datetime.now().replace(tzinfo=pytz.utc).timestamp())
        connection = sqlite3.connect(config.db_name)
        records = (connection.execute(GET_COUNT_UNDELIVERED %(config.email_success_failure_database,FAILED_STATUS, curr_time - config.undeliverable_period, curr_time))).fetchall()
        return  int(records[0][0]) > config.undeliverable_count
