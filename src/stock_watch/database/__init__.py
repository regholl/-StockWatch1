import logging
import os
import time

import psycopg2
import yaml

connection = None

def connect():
    global connection
    if connection is None:
        db_cred_dir = os.path.dirname(os.path.realpath(__file__)) + '/configs/database.yml'
        with open(db_cred_dir, 'r') as file:
            database_config = yaml.load(file, Loader=yaml.FullLoader)
            db_credentials = database_config['credentials']
            while True:
                try:
                    connection = psycopg2.connect(dbname=db_credentials['dbname'],
                                                  user=db_credentials['user'],
                                                  host=db_credentials['host'],
                                                  password=db_credentials['password'])
                    break
                except psycopg2.OperationalError:
                    logging.info("Waiting for database to start...")
                    time.sleep(1)
    return connection
