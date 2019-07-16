import sql
# class to write querie
NUM_ENTRIES_PER_PAGE = 100

def get_base_table(sql, curr_page = 0):
    query = f'SELECT * FROM A_TblCase LIMIT {NUM_ENTRIES_PER_PAGE * (curr_page +1 )} OFFSET {curr_page  * NUM_ENTRIES_PER_PAGE}'
    return (sql.SelectQuery(query,one = False))

#To get a new set of tables we need the following:
#1. The Query used to obtain the last set of tables
#2. The new column name and value to be added to the new query
#3. A list of tables used for the previous set of tables.
def new_tables(sql,currQuery,prevTables,addition):
    columnName = addition[columnName]
    value = addition[value]
    tablesQuery = "SELECT TABLE_NAME FROM data.INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = \'BASE TABLE\'"
    tables = sql.SelectQuery(tablesQuery,one=False)
    newQuery = currQuery + "AND "+columnName+"="+value

    #Find the tables that have this column
    tableMatch = []
    for table in tables:
        columns = get_columns(sql,table)
        numMatchingColumns = contains_query_columns(sql,currQuery,columns)
        if numMatchingColumns != 0:
            insertTable(numMatchingColumns,table,columns,tableMatch)

    response = []
    #Each entry of tableMatch is a tuple containing: (number of matching columns with new query, columns in current table, table Name)
    for table in tableMatch:
        newTable = {}
        newTable["tableName"] = table[2]
        newTable["colMatch"] = table[0]
        newTable["columns"] = table[1]

        #Get all the rows for this table
        query = "SELECT * FROM "+table[2]+" WhHERE "+newQuery
        rows = sql.SelectQuery(query,one=False)
        #TODO
        #1. Add each row to your newTable
        #2. Add it to response

    return response





def get_columns(sql,table):
    query = "SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME ="+table
    return (sql.SelectQuery(query,one = False))
