from sql import SQL



sql = SQL()
sql.connect()

tablesQuery = sql.ExecuteRaw("SHOW TABLES;")
tables = []
for table in tablesQuery:
    for k,v in table.items():
        column = sql.ExecuteRaw("SHOW COLUMNS FROM "+str(v))[1]["Field"]
        #print("Primary Key: "+str(column[1]["Field"]))
        try:
            sql.ExecuteRaw("ALTER TABLE "+str(v)+" ADD PRIMARY KEY("+column+")")
        except:
            print("WHOOPS: ")
