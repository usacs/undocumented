import React, { Component } from 'react';
import DisplayTable from './DisplayTable'
import  {getTable,getAllTablesForQuery} from '../api/api'
export default class Home extends Component {

   constructor(){
      this.state = {
         tablesToShow:[<DisplayTable table = "A_TblCase" onClickHandler ={this.onClickTest}/>]
      }
   }

   onClickTest(evt){
      const col = evt.target.getAttribute("column");
      const colVal = evt.target.getAttribute("name")
      getAllTablesForQuery(col,colVal).then(data=>{
          console.log(data);
      });
 }
    render() {
       return (
          <DisplayTable table = "A_TblCase" onClickHandler ={this.onClickTest}/>
       )
    }
}
