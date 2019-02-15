import datetime
import psycopg2
from.database import DatabaseConnection as db_conn

class User(db_conn):
    """docstring for User"""
    def __init__(self, user_data, isAdmin=0):
        self.firstname = user_data[0]
        self.lastname = user_data[1]
        self.othername = user_data[2]
        self.email = user_data[3]
        self.phoneNumber = user_data[4]
        self.passportUrl = user_data[5]
        self.password = user_data[6]
        self.isAdmin = isAdmin
    def create_new_user(self):
        """ creates/adds a new user to the users table"""
        query = """ INSERT INTO users(firstname, lastname, othername, Email,
         phoneNumber, PassportURL, isAdmin, password) VALUES('{}', '{}','{}','{}', '{}', '{}', '{}', '{}')    
        """.format(self.firstname , self.lastname , self.othername, self.email, self.phoneNumber,
        self.passportUrl, self.isAdmin, self.password)     
        self.save_incoming_data_or_updates(query)
    def loging(self, email, password):
        query =""" SELECT FROM users where Email={} AND passsword={} """.format( email, password)
        user = self.fetch_single_data_row(query)
        return user

