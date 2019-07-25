import React, { Component } from 'react'
import  {getTable,getAllTablesForQuery} from '../api/api'
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Paper from '@material-ui/core/Paper';
import { Tab } from '@material-ui/core';
/**
 * This component displays a table
 */
export default class DisplayTable extends Component{
    constructor(props){
        super(props)
        this.state = {
            columnNames : [],
            rows : [],
            page:0
        }
    }
    /**
     * On Mount make a request
     */
    componentDidMount(){
        const data = getTable(this.state.page,this.props.tableName)
        this.seralizeTable(data)
        this.seralizeData(DataCue)
    }
    /**
     * Set Table name and col info
     */
    seralizeTable(data) {
        const colnames = data.colnames;
        //Componets for the columns
        let colsComponents = []

        colnames.foreach(item=>{
            colsComponents.push(<TableCell>{item}</TableCell>)
        })
        this.setState({
            columnNames : colsComponents
        });
    }

    seralizeData(data){
        const rows = this.state.rows;
        for(let i=0;i<data.tableContent;i++){
            let rowData = []
            for(let j =0;j<data.tableContent[i];j++){
                rowData.push(<TableCell>{data.tableContent[i][j]}</TableCell>)
            }
            rows.push(<TableRow key = { data.tableContent[i][0]}>{rowData}</TableRow>)
            this.setState({
                rows:rows
            })
        }
        
    }

    /**
     * Display table info given the page and stuff
     */
    render(){
        return (
            <Paper className={this.props.table}>
            <Table className={this.props.table}>
              <TableHead>
                <TableRow>
                    {this.state.columnNames}
                </TableRow>
              </TableHead>
              <TableBody>
                {this.state.rows}
              </TableBody>
            </Table>
          </Paper>
        )   
    }

}