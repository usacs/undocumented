import sql
# class to write querie
NUM_ENTRIES_PER_PAGE = 100

def get_base_table(sql, curr_page = 0):
    query = f'SELECT * FROM A_TblCase LIMIT {NUM_ENTRIES_PER_PAGE * (curr_page +1 )} OFFSET {curr_page  * NUM_ENTRIES_PER_PAGE}' 
    return (sql.SelectQuery(query,one = False))


def new_tables(sql,curr_query,addition):
    columnName = addition[columnName]
    value = addition[value]






