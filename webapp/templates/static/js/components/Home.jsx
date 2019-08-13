import React, { Component } from 'react';
import DisplayTable from './DisplayTable'
import { getAllTablesForQuery } from '../api/api'
import Button from '@material-ui/core/Button';
import Axios from 'axios';
export default class Home extends Component {

   constructor() {
      super()
      this.onClickTest = this.onClickTest.bind(this)
      this.resetQuery = this.resetQuery.bind(this)
      this.state = {
         tablesToShow: [<DisplayTable table="A_TblCase" onClickHandler={this.onClickTest}></DisplayTable>]
      }
   }
   resetQuery(evt) {
      evt.preventDefault()
      console.log("Called")
      Axios.get('/reset').then(data => {
         /**
          * Reset the route
          */
         this.setState({
            tablesToShow: []
         })
         this.setState({
            tablesToShow: [<DisplayTable table="A_TblCase" onClickHandler={this.onClickTest}></DisplayTable>]
         });
      })
   }

   onClickTest(evt) {
      const col = evt.target.getAttribute("column");
      const colVal = evt.target.getAttribute("name")
      getAllTablesForQuery(col, colVal).then(data => {
         let newData = []
         data['tables'].forEach(data => {
            newData.push(<DisplayTable table={data['tableName']} onClickHandler={this.onClickTest}></DisplayTable>)
         })
         this.setState({
            tablesToShow: []
         })


         this.setState({
            tablesToShow: newData
         })
         console.log(this.state)


      });
   }
   render() {
      return (
         <div>
            <Button variant="contained" onClick={this.resetQuery}>
               RestQuery
            </Button>
            <div>
               {this.state.tablesToShow}
            </div>
         </div>


      )
   }
}
