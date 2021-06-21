# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 14:47:47 2021

@author: Muhammad Rizky Perdana
"""
# import required modules
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
import datetime
    
# connect python with mysql with your hostname, username, password and database
db= MySQLdb.connect(host='localhost',user='root',password='',database='sawapp', autocommit=True)
    
# get cursor object
cursor= db.cursor()   
    
# get current date and year
today = datetime.date.today()
today_date = today.strftime('%d-%m-%Y') 
year = today_date.split('-')
year = year[2]
    
# Close DB Connection
def dbclose(db=db):
    db.close()
    
#Execution by custom query
def exec_query(query, cursor=cursor):
    try:
        cursor.execute(query)
    except:
        print('Error query')
    
#Fetch all data from table (not tested)
def fetch_all_by_table(table, cursor=cursor):
    try:
        cursor.execute("Select * FROM " + table)
        result = cursor.fetchall()
        return result
    except:
        print('Error query')
            
#Insert data to admin table
def insert_admin(nik, username, password, cursor=cursor, db=db):
    try:
        cursor.execute("SELECT MAX(id_admin) FROM admin")
        id_admin = cursor.fetchone()
        if id_admin[0] == None:
            id_admin = [0]
        else:
            id_admin = id_admin[0] + 1
        cursor.execute("""INSERT INTO 
                   admin 
                   (id_admin, nik, username, password) 
               VALUES
                   (%(id_admin)s, %(nik)s, %(username)s, %(password)s)""", 
        {'id_admin': id_admin, 
         'nik': nik, 
         'username': username, 
         'password': password})
        ##db.commit()
    except:
        print("Query error")
        
#Update data admin (id, nik, username, password)
def update_admin(data, cursor=cursor, db=db):
    try:
        cursor.execute("""UPDATE
                   admin
                   SET
                   username = %(username)s, password = %(password)s
                   WHERE 
                   nik = %(nik)s
                   """, 
        {'nik': data[1], 
         'username': data[2],
         'password': data[3]})
        ##db.commit()
    except:
        print("Query error")


#Delete data admin (id, nik, username, password)
def delete_admin(data, cursor=cursor, db=db):
    try:
        cursor.execute("""DELETE FROM
                   admin
                   WHERE 
                   nik = %(nik)s
                   """, 
        {'nik': data[1]})
        ##db.commit()
    except:
        print("Query error")


            
#Insert data to penilaian table
def insert_penilaian(nik_penilai, status_penilaian = 0, tgl_penilaian=today, tahun_penilaian=year, cursor=cursor, db=db):
    try:
        cursor.execute("SELECT MAX(id_penilaian) FROM penilaian")
        id_penilaian = cursor.fetchone()
        if id_penilaian[0] == None:
            id_penilaian = [0]
        else:
            id_penilaian = id_penilaian[0] + 1
        cursor.execute("""INSERT INTO 
                   penilaian 
                   (id_penilaian, nik_penilai, tgl_penilaian, tahun_penilaian, status_penilaian) 
               VALUES
                   (%(id_penilaian)s, %(nik_penilai)s, %(tgl_penilaian)s, %(tahun_penilaian)s, %(status_penilaian)s)""", 
        {'id_penilaian': id_penilaian, 
         'nik_penilai': nik_penilai, 
         'tgl_penilaian': tgl_penilaian, 
         'tahun_penilaian': tahun_penilaian,
         'status_penilaian': status_penilaian})
        return id_penilaian
        ##db.commit()
    except:
        print("Query error")

#Update status penilaian (id_penilaian)
def approve_status_penilaian(id_penilaian):
    try:
        cursor.execute("""UPDATE
                   penilaian
                   SET
                   status_penilaian = 1
                   WHERE 
                   id_penilaian = %(id_penilaian)s
                   """, 
        {'id_penilaian': id_penilaian})
        ##db.commit()
    except:
        print("Query error")
        

#Insert  data to penilai table
def insert_penilai(nik, username, password,cursor=cursor, db=db):
    try:
        cursor.execute("SELECT MAX(id_penilai) FROM penilai")
        id_penilai = cursor.fetchone()
        if id_penilai[0] == None:
            id_penilai = [0]
        else:
            id_penilai = id_penilai[0] + 1
        cursor.execute("""INSERT INTO 
                   penilai 
                   (id_penilai, nik, username, password) 
               VALUES
                   (%(id_penilai)s, %(nik)s, %(username)s, %(password)s)""", 
        {'id_penilai': id_penilai, 
         'nik': nik, 
         'username': username, 
         'password': password})
        ##db.commit()
    except:
        print("Query error")
 
#Update data penilai (id, nik, username, password)
def update_penilai(data, cursor=cursor, db=db):
    try:
        cursor.execute("""UPDATE
                   penilai
                   SET
                   username = %(username)s, password = %(password)s
                   WHERE 
                   nik = %(nik)s
                   """, 
        {'nik': data[1], 
         'username': data[2],
         'password': data[3]})
        ##db.commit()
    except:
        print("Query error")
        
#Delete data penilai (id, nik, username, password)
def delete_penilai(data, cursor=cursor, db=db):
    try:
        cursor.execute("""DELETE FROM
                   penilai
                   WHERE 
                   nik = %(nik)s
                   """, 
        {'nik': data[1]})
        #db.commit()
    except:
        print("Query error")
        
#Insert data to karyawan table
def insert_karyawan(nik, nama, tempat_lahir, tgl_lahir, jabatan, tahun_masuk, cursor=cursor, db=db):
    try:
        tgl_lahir = datetime.datetime.strptime(tgl_lahir, '%d-%m-%Y')
        cursor.execute("""INSERT INTO 
                   karyawan 
                   (nik, nama, tempat_lahir, tgl_lahir, jabatan, tahun_masuk) 
               VALUES
                   (%(nik)s, %(nama)s, %(tempat_lahir)s, %(tgl_lahir)s, %(jabatan)s, %(tahun_masuk)s)""", 
        {'nik': nik, 
         'nama': nama,
         'tempat_lahir': tempat_lahir, 
         'tgl_lahir': tgl_lahir, 
         'jabatan': jabatan, 
         'tahun_masuk': tahun_masuk})
        #db.commit()
    except:
        print("Query error")    

#Update Karyawan (nik, nama, tempat_lahir, tgl_lahir, jabatan, tahun_masuk)        
def update_karyawan(data, cursor=cursor, db=db):
    try:
        tgl_lahir = datetime.datetime.strptime(data[3], '%d-%m-%Y')
        cursor.execute("""UPDATE
                   karyawan
                   SET
                   nama =  %(nama)s, tempat_lahir = %(tempat_lahir)s, tgl_lahir = %(tgl_lahir)s, jabatan = %(jabatan)s, tahun_masuk = %(tahun_masuk)s
                   WHERE 
                   nik = %(nik)s
                   """, 
        {'nik': data[0], 
         'nama': data[1],
         'tempat_lahir': data[2],
         'tgl_lahir': tgl_lahir,
         'jabatan': data[4],
         'tahun_masuk': data[5]})
        db.commit()
    except:
        print("Query error")

#Delete Karyawan (nik, nama, tempat_lahir, tgl_lahir, jabatan, tahun_masuk)                
def delete_karyawan(data, cursor=cursor, db=db):
    cursor.execute("SELECT * FROM admin WHERE nik = %(nik)s", {'nik' : data[0]})
    admin = cursor.fetchone()
    if admin == False:
        pass
    else:
        try:
            cursor.execute("""DELETE FROM
                   admin
                   WHERE 
                   nik = %(nik)s
                   """, 
                   {'nik': data[0]})
            #db.commit()    
        except:
            print('Query Error')
    cursor.execute("SELECT * FROM penilai WHERE nik = %(nik)s", {'nik' : data[0]})
    penilai = cursor.fetchone()
    if penilai == False:
        pass
    else:
        try:
            cursor.execute("""DELETE FROM
                   penilai
                   WHERE 
                   nik = %(nik)s
                   """, 
                   {'nik': data[0]})
            #db.commit()    
        except:
            print('Query Error')
    try:
        cursor.execute("""DELETE FROM
                   karyawan
                   WHERE 
                   nik = %(nik)s
                   """, 
        {'nik': data[0]})
        #db.commit()
    except:
        print("Query error")   
        
        
#Insert data to isi_penilaian
def insert_isi_penilaian(id_penilaian, data, masa_kerja, penilaian_kerja, perilaku, db=db, cursor=cursor):
    try:
        id_isi_penilaian = str(data[0])+str(id_penilaian)
        cursor.execute("""INSERT INTO 
                   isi_penilaian 
                   (id_isi_penilaian, id_penilaian, nik_karyawan, nama, jabatan, masa_kerja, penilaian_kerja, perilaku) 
               VALUES
                   (%(id_isi_penilaian)s, %(id_penilaian)s, %(nik_karyawan)s, %(nama)s, %(jabatan)s,%(masa_kerja)s, %(penilaian_kerja)s, %(perilaku)s)""", 
        {'id_isi_penilaian': id_isi_penilaian, 
         'id_penilaian': id_penilaian,
         'nik_karyawan': data[0],
         'nama': data[1],
         'jabatan': data[4],
         'masa_kerja': masa_kerja,
         'penilaian_kerja': penilaian_kerja,
         'perilaku': perilaku})
        #db.commit()
    except:
        print("Query error")

#Update data to isi_penilaian (id_isi_penilaian, norm_masa_kerja, norm_penilaian_kerja, norm_perilaku, hasil)
def update_isi_penilaian(data, db=db, cursor=cursor):
    try:
        cursor.execute("""UPDATE
                   isi_penilaian
                   SET
                   norm_masa_kerja = %(norm_masa_kerja)s, norm_penilaian_kerja = %(norm_penilaian_kerja)s, norm_perilaku = %(norm_perilaku)s, hasil =  %(hasil)s
                   WHERE 
                   id_isi_penilaian = %(id_isi_penilaian)s
                   """, 
        {'id_isi_penilaian': data[0], 
         'norm_masa_kerja': data[1],
         'norm_penilaian_kerja': data[2],
         'norm_perilaku': data[3],
         'hasil': data[4]})
        #db.commit()
    except:
        print("Query error")

          
        
#Cek login admin
def check_login_admin(username, password, cursor=cursor, db=db):
    try:
        cursor.execute("""SELECT * FROM
                   admin 
               WHERE
               username = 
                   %(username)s""", 
        {'username': username, })
        check = cursor.fetchone()
        if(check != None):
            if(check[2] == password):
                return True
            else:
                return False
        else:
            return False
    except:
        print('Query Error')
        return False    

#Cek login penilai
def check_login_penilai(username, password, cursor=cursor, db=db):
    try:
        cursor.execute("SELECT * FROM penilai WHERE username =  %(username)s", 
        {'username': username})
        check = cursor.fetchone()
        if(check != None):
            if(check[3] == password):
                return True
            else:
                return False
        else:
            return False
    except:
        print('Query Error')
        return False   
    
#Find by Nik (fetch one) (nik)
def find_by_nik(nik):
    try:
        cursor.execute("SELECT * FROM karyawan WHERE nik =  %(nik)s", 
        {'nik': nik})
        value = cursor.fetchone()
        if(value != None):
            return value
        else:
            return False
    except:
        print('Query Error')
        return False       
    
#Find by id_penilaian
def find_by_id_penilaian(id_penilaian):
    try:
        cursor.execute("SELECT * FROM isi_penilaian WHERE id_penilaian =  %(id_penilaian)s", 
        {'id_penilaian': id_penilaian})
        value = cursor.fetchall()
        if(value != None):
            return value
        else:
            return False
    except:
        print('Query Error')
        return False   

#Show output akhir by rank    
def show_rank(id_penilaian):
    try:
        cursor.execute("SELECT * FROM isi_penilaian WHERE id_penilaian =  %(id_penilaian)s ORDER BY hasil ASC", 
        {'id_penilaian': id_penilaian})
        value = cursor.fetchall()
        if(value != None):
            return value
        else:
            return False
    except:
        print('Query Error')
        return False   