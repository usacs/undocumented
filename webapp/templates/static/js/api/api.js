/**
 * Extract the table info 
 */
import Axios from 'axios'
export async function getTable(page, tableName){
    const resp = await Axios.post("/get-table",{"page":page, "table":tableName})
    return resp.data
}

export async function getAllTablesForQuery(columnName,columnValue){
    const resp = await Axios.post("/new-query",{"columnName":columnName, "value":columnValue})
    return resp.data
        
}

