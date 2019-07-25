/**
 * Extract the table info 
 */
import Axios from 'axios'
export async function getTable(page, tableName){
    Axios.post("/get-table",{"page":page, "table":tableName}).then(resp=>{
        return resp.data;
    })
}

export async function getAllTablesForQuery(columnName,columnValue){
    Axios.post("/new-query",{"columnName":columnName, "value":columnValue}).then(resp=>{
        return resp.data
    })
}

