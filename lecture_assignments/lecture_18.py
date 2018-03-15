
import sqlite3
import sys

def init_db():
    conn = sqlite3.connect('teaching.db')
    cur = conn.cursor()

    # Drop tables
    statement = '''
        DROP TABLE IF EXISTS 'Instructors';
    '''
    cur.execute(statement)
    statement = '''
        DROP TABLE IF EXISTS 'Classes';
    '''
    cur.execute(statement)

    conn.commit()

    statement = '''
        CREATE TABLE 'Instructors' (
            'Id' INTEGER PRIMARY KEY AUTOINCREMENT,
            'LastName' TEXT NOT NULL,
            'FirstName' TEXT NOT NULL,
            'Uniqname' TEXT NOT NULL,
            'Office' TEXT
        );
    '''
    cur.execute(statement)
    statement = '''
        CREATE TABLE 'Classes' (
                'Id' INTEGER PRIMARY KEY AUTOINCREMENT,
                'CourseDept' TEXT NOT NULL,
                'CourseNum' TEXT NOT NULL,
                'TeacherId' INTEGER
        );
    '''
    cur.execute(statement)
    #make sure to commit to actually make the changes happen
    conn.commit()
    conn.close()

if len(sys.argv) > 1 and sys.argv[1] == '--init':
    print('Deleting db and starting over from scratch.')
    init_db()
else:
    print('Leaving the DB alone.')


def insert_stuff():
    conn = sqlite3.connect('teaching.db')
    cur = conn.cursor()

    instructors = [['Mark', 'Newman', 'mwnewman', '4380 NQ'],
                   ['Jackie', 'Cohen', 'jczetta', '3333 NQ'],
                   ['Steven', 'Oney', 'soney', '4366 NQ']]

    for inst in instructors:
        insertion = (None, inst[0], inst[1], inst[2], inst[3])
        statement = 'INSERT INTO "Instructors" '
        statement += 'VALUES (?, ?, ?, ?, ?)'
        cur.execute(statement, insertion)

    conn.commit()
    conn.close()



def update_stuff():
    conn = sqlite3.connect('teaching.db')
    cur = conn.cursor()

    new_office = '4445 NQ'
    uniqname = 'mwnewman'
    t = (new_office, uniqname)
    statement = 'UPDATE Instructors '
    statement += 'SET Office=? '
    statement += 'WHERE Uniqname=?'
    print(statement)
    cur.execute(statement, t)

    conn.commit()
    conn.close()

def delete_mark_newman():
    conn = sqlite3.connect('teaching.db')
    cur = conn.cursor()

    statement = 'DELETE FROM Instructors'
    statement += 'WHERE LastName="Newman"'
    cur.execute(statement)
    conn.commit()
    conn.close()
