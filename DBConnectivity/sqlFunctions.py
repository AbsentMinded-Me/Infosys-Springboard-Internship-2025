from connection import get_db_connection
import mysql.connector
from mysql.connector import Error
from fastapi import APIRouter

router = APIRouter()

#to create a new user
@router.post('/create/user')
def create_user(name, email, password):
    try:
        db = get_db_connection()
        cursor = db.cursor(dictionary=True)
        query = 'insert into tbluser(name, email, password) values(%s, %s, %s)'
        cursor.execute(query, (name, email, password))
        db.commit()
        return {'message': 'User created successfully'}
    except Error as e:
        return {'error': str(e)}
    finally:
        cursor.close()
        db.close()

#to get user by id
@router.get('/get/user_by_id')
def get_user_by_id(user_id):
    try:
        db = get_db_connection()
        cursor = db.cursor(dictionary=True)
        query = 'select * from tbluser where id = %s'
        cursor.execute(query, (user_id,))
        user = cursor.fetchone()
        if user:
            return user
        else:
            return {'message': 'User not found'}
    except Error as e:
        return {'error': str(e)}
    finally:
        cursor.close()
        db.close()

#to update user details
@router.put('/update/user')
def update_user(user_id, name=None, email=None, password=None):
    try:
        db = get_db_connection()
        cursor = db.cursor(dictionary=True)
        fields = []
        values = []
        if name:
            fields.append('name = %s')
            values.append(name)
        if email:
            fields.append('email = %s')
            values.append(email)
        if password:
            fields.append('password = %s')
            values.append(password)
        values.append(user_id)
        query = f'update tbluser set {", ".join(fields)} where id = %s'
        cursor.execute(query, tuple(values))
        db.commit()
        return {'message': 'User updated successfully'}
    except Error as e:
        return{'error': str(e)}
    finally:
        cursor.close()
        db.close()

#to delete user
@router.delete('/delete/user')
def delete_user(user_id):
    try:
        db = get_db_connection()
        cursor = db.cursor(dictionary=True)
        query = 'delete from tbluser where id = %s'
        cursor.execute(query, (user_id,))
        db.commit()
        return {'message': 'User deleted successfully'}
    except Error as e:
        return {'error': str(e)}
    finally:
        cursor.close()
        db.close()