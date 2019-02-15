import os

def drop_table_if_exists():
    """ Deletes all tables"""
    drop_users = """ DROP TABLE IF EXISTS users """
    return [drop_users]
def set_up_tables():
    create_users_table = """
        CREATE TABLE users(id INT PRIMARY KEY NOT NULL, 
        firstname CHAR(50) NOT NULL,
        lastname CHAR(50) NOT NULL,
        othername CHAR(50) NOT NULL,
        Email CHAR(50) NOT NULL,
        phoneNumber VARCHAR(20) NOT NULL,
        PassportUrl VARCHAR(20) NOT NULL,
        password VARCHAR(20) NOT NULL,
        isAdmin INT NOT NULL);"""
    
    return [create_users_table]

def create_admin(connect):
    query = """
        INSERT INTO users(firstname, lastname, othername, Email, phoneNumber,
        PassportURL, isAdmin, password) VALUES(1,'jacks', 'ks', 'ws', 'me@.com', 0834323423, 
        'pasport/pasport', 'jspon' 1);"""

    # prevents trying duplicating admin if already exists
    get_admin = """SELECT * from users where isAdmin = 1'"""
    cur = connect.cursor()
    get_admin = cur.execute(get_admin)
    get_admin = cur.fetchone()
    if get_admin:
        pass
    else:
        cur.execute(query)
        connect.commit()