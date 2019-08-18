# undocumentedNY

This project is to support the DocumentedNY team. 

## Setting up
First you're going to have to setup an AWS RDS instance for the data. Unfortantely this is not a simple task. 
First download https://fileshare.eoir.justice.gov/FOIA-TRAC-Report.zip. This contains all the CSVS needed. 

Next you need to load the data.
You can load the data in any way you please, but the best way is to use the load_into_table.py script. This script loads the first 3000 rows into a db. (Note: You Should replace the user and password and stuff with your own information). This uses pandas to load the csv into a dataframe and puts it into a SQL db. For testing 3000 rows are fine but realistically you would want the whole thing.

## Setting the primary keys.
the `sqlThings/` folder has a file for setting the primary keys. If you run that it will try to set the primary keys.Note: You need to set up a config file in the same direcotry. Look at this for an example  https://github.com/Sail338/undocumented/blob/master/webapp/templates/src/driver/config.py.example.

## Running the Webapp

### MAKE SURE TO MAKE A CONFIG.PY FOLLWOING THIS EXAMPLE WITH YOUR DB INFO  https://github.com/Sail338/undocumented/blob/master/webapp/templates/src/driver/config.py.example.
```
cd `webapp/templates/static #cd into react app
npm install
num run-script watch  #adds hot reloading, not there is a bug with caching so every time you reload the browswer you have to do a hard cache reset 

# for the flask app
cd webApp
python run.py
```
## Explanation of WebApp
On loading the webapp `localhost:5000` you will see the base table, A_tblCase. On Clicking on K/V Pair (A cell) You get all the tables that have that entry

### Todos
- Clean up UI
- Make sure this scales properly when all the data is included
- Add some searching features
