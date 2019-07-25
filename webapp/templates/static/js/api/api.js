/**
 * Extract the table info 
 */
import Axios from 'axios'
export async function getTable(page, tableName){
    Axios.get("/get_table",{"page":page, "table":tableName}).then(resp=>{
        return resp.data;
    })
}

