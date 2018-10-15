

import sqlite3
import config

def create_db_and_tables():
    """
    Creates 4 tables in DB when run for the first time as per config
    """
    connection = sqlite3.connect(config.db_name)

    connection.execute("""CREATE TABLE IF NOT EXISTS `%s` (
                            `sender_email` VARCHAR(256) NOT NULL,
                            `date_in_epoch` INT NOT NULL,
                            `count` INT NOT NULL,
                            PRIMARY KEY (`sender_email`,`date_in_epoch`))"""
                            %(config.email_timestamp_database_name))
    connection.execute("""CREATE TABLE IF NOT EXISTS `%s` (
                            `sender` VARCHAR(256) NOT NULL,
                            `receiver` VARCHAR(256) NOT NULL,
                            `content` VARCHAR(1048576) NOT NULL,
                            `time_stamp` INT NOT NULL,
                            `status` INT NOT NULL,
                            PRIMARY KEY (`sender`,`receiver`,`content`)
                        )""" %(config.email_success_failure_database))  #status 0 mean failed, status 1 success

    connection.execute("""CREATE TABLE  IF NOT EXISTS `%s` (
                                `email` VARCHAR(256) NOT NULL,
                                `password` VARCHAR(256) NOT NULL,
                                 PRIMARY KEY (`email`)
                            )""" %(config.email_senders_table_name))

    connection.execute("""CREATE TABLE  IF NOT EXISTS `%s` (
                                    `email_domain` VARCHAR(256) NOT NULL,
                                    `smtp_host` VARCHAR(256) NOT NULL,
                                    `smtp_port` VARCHAR(256) NOT NULL,
                                     CONSTRAINT PK_SMTP PRIMARY KEY (`email_domain`)
                                )""" % (config.smtp_host_details_table_name))

    connection.close()
