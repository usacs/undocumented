import React, { Component } from 'react';
import DisplayTable from './DisplayTable'
import  {getTable,getAllTablesForQuery} from '../api/api'
export default class Home extends Component {

   constructor(props){
      super(props)
      this.onClickTest = this.onClickTest.bind(this)
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
          data['tables'].forEach(data =>{
             newData.push(<DisplayTable table = {data['tableName']} onClickHandler ={this.onClickTest}></DisplayTable>)
          })
   
          this.setState({
             tablesToShow:newData
          })

          
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
