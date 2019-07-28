import React, { Component } from 'react';
import DisplayTable from './DisplayTable'
import  {getTable,getAllTablesForQuery} from '../api/api'
export default class Home extends Component {

   constructor(){
      super()
      this.state = {
         tablesToShow:[<DisplayTable table = "A_TblCase" onClickHandler ={this.onClickTest}></DisplayTable>]
      }
   }

   onClickTest(evt){
      const col = evt.target.getAttribute("column");
      const colVal = evt.target.getAttribute("name")
      getAllTablesForQuery(col,colVal).then(data=>{
          console.log(data);
          let newData = []

          
      });
      
 }
    render() {
       return (
          <div>
               {this.state.tablesToShow}
          </div>
          
       )
    }
}
