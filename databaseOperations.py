import sqlite3

# CONNECT TO DATABASE

DATA_LOC = "./DataBase.db"

# def init():
#     conn = sqlite3.connect(DATA_LOC)
#     cur = conn.cursor()

def get_globals():
    conn = sqlite3.connect(DATA_LOC)
    cur = conn.cursor()
    cur.execute("SELECT * FROM Globals")
    data = cur.fetchone()
    conn.commit()
    conn.close()
    return data

def update_globals(data):
    conn = sqlite3.connect(DATA_LOC)
    cur = conn.cursor()
    cur.execute("UPDATE Globals SET date = (?) ,invoice_number = (?) ",(data[0],data[1]))
    conn.commit()
    conn.close()


def insert_data(data,column_names,table_name):
    """
    will put data into database
    @param data: list of data
    @param column_names: list of columns
    @param table_name: list of tables
    """
    column_str = "("
    for name in column_names[:-1]:
        column_str += str(name)
        column_str += ","

    column_str += str(column_names[-1])
    column_str += ")"

    values_str = "("
    for name in column_names[:-1]:
        values_str += "?"
        values_str += ","

    values_str += "?"
    values_str += ")"

    conn = sqlite3.connect(DATA_LOC)
    cur = conn.cursor()
    sql = '''INSERT INTO {0} {1} 
             VALUES {2}'''.format(table_name,column_str,values_str)
    cur.execute(sql,data)
    conn.commit()
    conn.close()



def update_or_create(id_, data,column_names,table_name):
    """
    Will put data into database
    @param ID: ID of document to avoid duplications (rowid)
    @param input: list of data
    @param cols: list of columns
    @param tables: list of tables 
    """

    conn = sqlite3.connect(DATA_LOC)
    cur = conn.cursor()

    column_str = ""
    for name in column_names[:-1]:
        column_str += str(name)
        column_str += " = (?) ,"

    column_str += str(column_names[-1])
    column_str += " = (?) "

    sql = '''UPDATE {0} 
             SET {1}
             WHERE rowid = (?)'''.format(table_name,column_str)

    tuple_ = []
    for d in data:
        tuple_.append(d)
    tuple_.append(str(id_))
    cur.execute(sql,tuple(tuple_))
    print("updated")
    conn.commit()
    conn.close()


def get_single_data(id_,table_name):
    """
    Will get multiple line data from database using date
    @param date: date of invoice
    @param table_name: name of the table
    @return: list of data
    """

    conn = sqlite3.connect(DATA_LOC)
    cur = conn.cursor()
    sql = '''SELECT rowid,* 
             FROM {0}
             WHERE rowid = (?)'''.format(table_name)
    str_id = str(id_)
    cur.execute(sql,str_id)
    data = cur.fetchone()
    conn.commit()
    conn.close()
    return data

def get_multiple_data(table_name):
    """
    Will get multiple line data from database using table name
    @param tables: name of the table
    @return: list of data
    """
    conn = sqlite3.connect(DATA_LOC)
    cur = conn.cursor()
    sql = '''SELECT rowid,* FROM {0}'''.format(table_name)
    cur.execute(sql)
    data = cur.fetchall()
    conn.commit()
    conn.close()
    return list(data)

def get_multiple_data_invoice(id_,table_name):
    """
    Will get multiple line data from database using invoice ID
    @param ID: ID of invoice
    @param tableName: name of the table
    @return: list of data
    """
    conn = sqlite3.connect(DATA_LOC)
    cur = conn.cursor()
    sql = '''SELECT rowid,* 
             FROM {0}
             WHERE invoice_number = (?)'''.format(table_name)
    str_id = str(id_)
    cur.execute(sql,str_id)
    data = cur.fetchall()
    conn.commit()
    conn.close()
    return data

def get_multiple_data_days(date,table_name):
    """
    Will get multiple line data from database using date
    @param date: date of invoice
    @param table_name: name of the table
    @return: list of data
    """
    date_ = "Date"
    conn = sqlite3.connect(DATA_LOC)
    cur = conn.cursor()
    sql = '''SELECT rowid,* 
             FROM {0}
             WHERE {1} = (?)'''.format(table_name,date_)
    str_id = str(date)
    cur.execute(sql,str_id)
    data = cur.fetchall()
    conn.commit()
    conn.close()
    print(sql)
    print(date)
    print("Data: ")
    print(data)
    return data

def update_existing_stock(vol,vendor,part,vehicle):
    """
    Will update previous stock (subtract)
    @param vol: volume of stock
    @param vendor: vendor of stock
    @param part: name of the part
    @param vehicle: name of the vehicle
    @return: True
    """
    conn = sqlite3.connect(DATA_LOC)
    cur = conn.cursor()

    cur.execute('''UPDATE Stats 
             SET stock = stock - (?)
             WHERE vendor_name = (?) AND
             part_name = (?) AND
             vehicle_type = (?) ''',(vol,vendor,part,vehicle))
    data = cur.fetchone()
    conn.commit()
    conn.close()
    return True

def update_existing_stock_add(vol,vendor,part,vehicle):
    """
    Will update previous stock (add)
    @param vol: volume of stock
    @param vendor: vendor of stock
    @param part: name of the part
    @param vehicle: name of the vehicle
    @return: True
    """
    conn = sqlite3.connect(DATA_LOC)
    cur = conn.cursor()

    cur.execute('''UPDATE Stats 
             SET stock = stock + (?)
             WHERE vendor_name = (?) AND
             part_name = (?) AND
             vehicle_type = (?) ''',(vol,vendor,part,vehicle))
    data = cur.fetchone()
    conn.commit()
    conn.close()
    return True

#Update Threshold
def update_existing_Threshold(days,vol,part,vehicle):
    """
    Will update threshold
    @param days: days to threshold
    @param vol: volume of stock
    @param part: name of the part
    @param vehicle: name of the vehicle
    @return: True
    """
    conn = sqlite3.connect(DATA_LOC)
    cur = conn.cursor()

    cur.execute('''UPDATE Parts 
             SET Threshold = Threshold  + ((?)/(?))
             WHERE part_name = (?) AND
             vehicle_type = (?) ''',(vol,days,part,vehicle))
    data = cur.fetchone()
    conn.commit()
    conn.close()
    return True

def update_existing(id_, data,column_names,table_name):
    """
    Will update current stock
    @param ID: ID of document
    @param data: data to update
    @param columns: columns corresponding data to be updated
    @param tableName: name of the table
    @return: True
    """
    conn = sqlite3.connect(DATA_LOC)
    cur = conn.cursor()

    column_str = ""
    for name in column_names[:-1]:
        column_str += str(name)
        column_str += " = (?) ,"

    column_str += str(column_names[-1])
    column_str += " = (?) "

    sql = '''UPDATE {0} 
             SET {1}
             WHERE rowid = (?)'''.format(table_name,column_str)


    tuple_ = []
    for d in data:
        tuple_.append(d)
    tuple_.append(str(id_))

    cur.execute(sql,tuple(tuple_))
    data = cur.fetchone()
    conn.commit()
    conn.close()
    return True


def remove_data(id_,table_name):
    '''
    Will remove data from database
    @param ID: ID of document to remove
    @param tableName: name of the table
    '''    
    conn = sqlite3.connect(DATA_LOC)
    cur = conn.cursor()
    str_id = str(id_)
    cur.execute('''DELETE FROM {0} WHERE rowid = (?)'''.format(table_name),(str_id,))
    conn.commit()
    conn.close()

def remove_data_from_list(details,data,table_name):
    '''
    Will remove data from database
    @param details: details of document to remove
    @param data: data to remove
    @param tableName: name of the table
    '''
    conn = sqlite3.connect(DATA_LOC)
    cur = conn.cursor()
    table_name = "Stats"
    tuple_ = []
    if len(details) == 1:
        sql = '''DELETE FROM {0} WHERE vendor_name = (?) AND part_name = (?) AND vehicle_type = (?)'''.format(table_name)
        tuple_.append(details[0])
        tuple_.append(data[0])
        tuple_.append(data[1])
        print(tuple_)
        cur.execute(sql,tuple(tuple_))

    else:
        sql = '''DELETE FROM {0} WHERE vendor_name = (?) AND part_name = (?) AND vehicle_type = (?)'''.format(table_name)
        tuple_.append(data[0])
        tuple_.append(details[0])
        tuple_.append(details[1])
        cur.execute(sql,tuple(tuple_))

    
    conn.commit()
    conn.close()

def remove_data_vendor_part(details,table_name):
    conn = sqlite3.connect(DATA_LOC)
    cur = conn.cursor()
    table_name = "Stats"
    tuple_ = []
    if len(details) == 1: #Vendor
        tuple_.append(details[0])
        cur.execute('''DELETE FROM Vendors WHERE name = (?)''',tuple(tuple_))
        sql = '''DELETE FROM {0} WHERE vendor_name = (?)'''.format(table_name)
        
        cur.execute(sql,tuple(tuple_))

    else:
        tuple_.append(details[0])
        tuple_.append(details[1])
        
        cur.execute('''DELETE FROM Parts WHERE part_name = (?) AND vehicle_type = (?)''',tuple(tuple_))
        sql = '''DELETE FROM {0} WHERE part_name = (?) AND vehicle_type = (?)'''.format(table_name)
        cur.execute(sql,tuple(tuple_))
    
    conn.commit()
    conn.close()


def get_threshold(details):
    conn = sqlite3.connect(DATA_LOC)
    cur = conn.cursor()
    tuple_ = []
    tuple_.append(details[0])
    tuple_.append(details[1])
    cur.execute('''SELECT Threshold FROM Parts
             WHERE part_name = (?) AND
             vehicle_type = (?) ''',tuple(tuple_))
    data = cur.fetchone()
    conn.commit()
    conn.close()
    print(data)
    return int(data[0])

def get_stocksum(details):
    conn = sqlite3.connect(DATA_LOC)
    cur = conn.cursor()
    tuple_ = []
    tuple_.append(details[0])
    tuple_.append(details[1])
    cur.execute('''SELECT * FROM Stats
             WHERE part_name = (?) AND
             vehicle_type = (?) ''',tuple(tuple_))
    data = cur.fetchall()
    sum_ = 0
    for d in data:
        sum_ += int(d[3])

    conn.commit()
    conn.close()
    return sum_

# def close():
#     conn = sqlite3.connect(DATA_LOC)
#     conn.commit()
#     conn.close()