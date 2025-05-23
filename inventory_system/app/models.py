from flask_mysqldb import MySQL

mysql = MySQL()

def insert_device(data):
    cur = mysql.connection.cursor()
    cur.execute("""
        INSERT INTO devices (hostname, ip_address, os, cpu, ram_gb)
        VALUES (%s, %s, %s, %s, %s)
    """, (data['hostname'], data['ip_address'], data['os'], data['cpu'], data['ram_gb']))
    mysql.connection.commit()
    cur.close()

def get_all_devices():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM devices")
    results = cur.fetchall()
    cur.close()
    return results
