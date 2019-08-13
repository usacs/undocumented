import React, { Component } from 'react'
import { getTable, getAllTablesForQuery } from '../api/api'
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Paper from '@material-ui/core/Paper';

/**
 * This component displays a table
 */
export default class DisplayTable extends Component {
    constructor(props) {
        super(props)

        this.state = {
            columnNames: [],
            rows: [],
            page: 0
        }

    }
    /**
     * On Mount make a request
     */
    componentDidMount() {
        getTable(this.state.page, this.props.table).then(data => {
            this.seralizeData(data)
            this.seralizeTable(data)
        })
    }


    getNextPage() {
        let page = this.state.page;
        page += 1
        this.setState({
            page: page
        })
        getTable(this.state.page, this.props.table).then(data => {
            console.log("serialzed the data")
            //from now on only grab next data
            this.seralizeData(data)
        })
    }


    /**
     * Set Table name and col info
     */
    seralizeTable(data) {
        const colnames = Object.keys(data[0]);
        //Componets for the columns
        let colsComponents = []

        colnames.forEach(item => {
            colsComponents.push(<TableCell>{item}</TableCell>)
        })
        this.setState({
            columnNames: colsComponents
        });
    }
    /**
     * 
     * Serialize the data from the flask request
     */
    seralizeData(data) {
        const rows = this.state.rows;
        for (let i = 0; i < data.length; i++) {
            let rowData = []
            for (let key in data[i]) {
                if (data[i].hasOwnProperty(key)) {
                    rowData.push(<TableCell column={key} name={data[i][key]} onClick={this.props.onClickHandler}>{data[i][key]}</TableCell>)
                }
            }

            rows.push(<TableRow key={data[i][0]}>{rowData}</TableRow>)
            this.setState({
                rows: rows
            })
        }

    }

    /**
     * Display table info given the page and stuff
     */
    render() {
        if (this.state.rows.length == 0 ) {
            return <div></div>
        }
        if(this.state.rows.length > 0){
            return (
                <Paper className={this.props.table}>
                    <h1>{this.props.table}</h1>
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

}