#!/usr/bin/env python
from passlib.hash import sha512_crypt as sha

class AccountsError(Exception):
    pass

def add_account(db, username, password):
    '''add_account(db, username, password) -> None
    add account to "users" database'''
    existing_user = db.execute(
        'SELECT username FROM users WHERE username=?',
        [username]
    ).fetchall()
    if existing_user:
        raise AccountsError('User already exists')
    else:
        salted_hash = sha.encrypt(password)
        print "Username: {0}\tPassword: {1}".format(username,salted_hash)
        db.execute(
            'INSERT INTO users (username, salted_hash) VALUES (?,?)',
            [username, salted_hash]
        )
        db.commit()
    

def verify_login(db, username, password):
    '''verify_login(db, username, password) -> (success, error)

    compare hashed password guess to actual hashed password
    
    "success" - True/False depending on whether the login was successful
    "error" - Error message if success=False, none if success=True 
    '''
    #get hashed_pw from database
    com = db.execute(
        'SELECT salted_hash FROM users WHERE username=?',
        [username]    
    ).fetchall()
    if com:
        hashed_pw = com[0][0]
    else:
        return (False, 'Invalid username!')

    #compare hash to inputted password
    if sha.verify(password, hashed_pw):
        return (True, None)
    else:
        return (False, 'Invalid password!')

def reset_password(db, username):
    '''reset_password(db,username) -> ???'''
    pass