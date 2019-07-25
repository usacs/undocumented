import React, { Component } from 'react'
import  {getTable,getAllTablesForQuery} from '../api/api'
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
/**
 * This component displays a table
 */
export default class DisplayTable extends Component{
    constructor(props){
        super(props)
        this.state = {
            columnNames : [],
            columnValues : [],
            page:0
        }
    }
    /**
     * On Mount make a request
     */
    componentDidMount(){
        const data = getTable(this.state.page,this.props.tableName)
    }
    /**
     * Set Table name and col info
     */
    seralizeTable(data) {
        const colnames = data.colnames;
    }
    seralizeData(data){
        const rows = []
        for(let i=0;i<data.tableContent;i++){
            
        }
    }

    /**
     * Display table info given the page and stuff
     */
    render(){
        return (
        
        )   
    }

}