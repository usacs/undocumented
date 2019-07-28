from sql import SQL
from operator import itemgetter
# class to write querie
NUM_ENTRIES_PER_PAGE = 100



def get_table(sql, newQuery, curr_page = 0,tableName='A_TblCase'):
    query = ""
    if len(newQuery) == 0:
        query = f'SELECT * FROM {tableName} LIMIT {NUM_ENTRIES_PER_PAGE * (curr_page +1 )} OFFSET {curr_page  * NUM_ENTRIES_PER_PAGE}'
    else:
        query = f'SELECT * FROM {tableName} WHERE {newQuery} LIMIT {NUM_ENTRIES_PER_PAGE * (curr_page +1 )} OFFSET {curr_page  * NUM_ENTRIES_PER_PAGE}'
    return (sql.SelectQuery(query,one = False))

#To get a new set of tables we need the following:
#1. The Query used to obtain the last set of tables
#2. The new column name and value to be added to the new query
#3. A list of tables used for the previous set of tables.
def new_tables(sql,oldQuery,addition):
    newData = {}
    columnName = addition['columnName']
    value = addition['value']
    tablesQuery = f"SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE'"
    tables = sql.SelectQuery(tablesQuery,one=False)
    if(oldQuery == ''):
        try:
            float(value)
            newQuery = f"{columnName}={value}"
        except ValueError:
            newQuery = f"{columnName}=\"{value}\""
    else:
        try:
            float(value)
            newQuery = f"{oldQuery} AND {columnName}={value}"
        except ValueError:
            newQuery = f"{oldQuery} AND {columnName}=\"{value}\""
    newData["currentQuery"] = newQuery

    #Find the tables that have this column
    tableMatch = []
    for table in tables:
        table_parsed = table['TABLE_NAME']
        columns = get_columns(sql,table_parsed)
        matchingAndQuery = contains_query_columns(sql,newQuery,columns)
        numMatchingColumns = matchingAndQuery[0]
        updatedQuery = matchingAndQuery[1]
        if numMatchingColumns != 0:
            insertTable(numMatchingColumns,table_parsed,columns,updatedQuery,tableMatch)
            print("Num Matching Cols: ", numMatchingColumns)

    newData["tables"] = []
    #Each entry of tableMatch is a tuple containing: (number of matching columns with new query, columns in current table, table Name)
    for table in tableMatch:
        newTable = {}
        newTable["tableName"] = table[0]
        newTable["numberOfMatchingColumns"] = table[1]

        #Get all the rows for this table

        query = f"SELECT * FROM {table[0]}  WHERE {table[3]}"
        print(query)
        newData["tables"].append(newTable)




    return newData

def insertTable(numMatchingColumns,table,columns,query,tableMatch):
    tableMatch.append( (table,numMatchingColumns,columns,query) )
    tableMatch.sort(key=itemgetter(1))
    return

#Looking at the current query check to see if all the columns exist in the list of coclumns specified
def contains_query_columns(sql,query,columns):
    numMatching = 0
    #Get the columns that we want:
    # Query Looks like this: a=3 AND b=2 AND c=5
    columnsList = query.replace(" ","").split("AND")
    #extracted out columns names from the returned JSON
    columnsParsed = []
    for i in range(0,len(columns)):
        #columns[i]['COLUMN_NAME'] = columns[i]['COLUMN_NAME'].upper()
        columnsParsed.append(columns[i]['COLUMN_NAME'].upper())
    i = 0
    while i < len(columnsList):
        if columnsList[i].split("=")[0].upper() in columnsParsed:
            numMatching +=1
        else:
            # If the column doesnt exist in the table, remove it so the query doesnt break
            del columnsList[i]
            i-=1
        i+=1
    newQuery = " AND ".join(columnsList)
    return (numMatching,newQuery)

def get_columns(sql,table):
    query = f"SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{table}'"
    return (sql.SelectQuery(query,one = False))
