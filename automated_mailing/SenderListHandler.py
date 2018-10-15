
import config
import  sqlite3
from CommonUtils import is_valid_email,is_valid_hostname, is_valid_port, \
    get_domain_from_email,get_domain_name_from_smtp_host, LOGGER_INFO, \
    LOGGER_WARNING, LOGGER_ERROR
import traceback


class SenderListHandler:
    """This class offers methods to handle sender email/password details
    It communicates with DB directly
    """
    def __init__(self):
        self.all_smtp_details = self.get_all_smtp()
        
    def insert_sender_email_into_db(self, email, password):
        if is_valid_email(email):
            try:
                connection = sqlite3.connect(config.db_name)
                connection.execute("INSERT INTO %s (email, password) VALUES ('%s', '%s')"
                                        %(config.email_senders_table_name, email,password))
                connection.commit()
                connection.close()
            except sqlite3.IntegrityError:
                print(LOGGER_WARNING + " Given username password already in database. Skipping Insertion. Email:%s Password: %s" %(email, password))
            except:
                print(LOGGER_ERROR + " Insert to db failed. Stack Trace: ")
                print(traceback.format_exc())
        else:
            print("You have provided incorrect email address")

    def insert_smtp_host_detail_into_db(self, email_domain, smtp_host, smtp_port):
        if is_valid_hostname(smtp_host) and is_valid_port(smtp_port):
            try:
                connection = sqlite3.connect(config.db_name)
                connection.execute("INSERT INTO %s (email_domain, smtp_host, smtp_port) VALUES ('%s','%s', '%s')"
                                        %(config.smtp_host_details_table_name, email_domain, smtp_host,smtp_port))
                connection.commit()
                connection.close()
            except sqlite3.IntegrityError:
                print(LOGGER_WARNING+" Given host & port already in database. Skipping Insertion.")
            except:
                print(LOGGER_ERROR +" Insert to db failed. Stack Trace: ")
                print(traceback.format_exc())
        else:
            print(LOGGER_WARNING +" You have provided incorrect hostname or the port value")

    def get_senders_list_from_email(self):
        try:
            connection = sqlite3.connect(config.db_name)
            rows = connection.execute("SELECT email,password FROM %s" %(config.email_senders_table_name))
            items = [{"email": x[0], "password": x[1]} for x in rows.fetchall()]
            connection.close()
            return  items
        except:
            print(LOGGER_ERROR+ " Select query Failed. Stack Trace: ")
            print(traceback.format_exc())
        return None

    def get_all_smtp(self):
        try:
            connection = sqlite3.connect(config.db_name)
            rows = connection.execute("SELECT email_domain,smtp_host,smtp_port FROM %s" %(config.smtp_host_details_table_name))
            items = {x[0]:{"smtp_host":x[1], "smtp_port":x[2]} for x in rows.fetchall()}
            connection.close()
            return items
        except:
            print(LOGGER_ERROR +" Select query Failed while fetching smtp_host & port for all email ids . Stack Trace: ")
            print(traceback.format_exc())
        return []

    def get_smtp_details_for(self, email):
        domain = get_domain_from_email(email)
        connection = sqlite3.connect(config.db_name)
        rows = connection.execute(
            "SELECT email_domain,smtp_host,smtp_port FROM %s WHERE email_domain='%s'" % (config.smtp_host_details_table_name,domain))
        item = rows.fetchall()
        connection.close()
        if item:
            return {"smtp_host":item[0][1], "smtp_port":item[0][2]}
        else:
            print(LOGGER_ERROR +" SMTP details not found for %s" %(email))
            return None


