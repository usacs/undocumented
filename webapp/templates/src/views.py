from flask import render_template, Blueprint, request, jsonify, session
import driver
from driver.sql import SQL
blueprint = Blueprint('src',__name__)
@blueprint.route('/')
def index():
 return render_template("index.html")

 @blueprint.route('/get-table',methods=("POST"))
 def getTable():
     sql = SQL()
     sql.connect()
     data = request.get_json()
     tableName = data["table"]
     page = int(data['page'])
     tableData = driver.get_table(sql,page,tableName)
     return jsonify(tableData)

@blueprint.route('/new-query',methods=["POST"])
def newQuery():
    sql = SQL()
    sql.connect()
    data = request.get_json()
    if "currQuery" not in session:
        session["currQuery"] = ""
    oldQuery = session["currQuery"]
    newData = driver.new_tables(sql,oldQuery,data)
    session["currQuery"] = newDatta["currentQuery"]
    return jsonify(newData)
