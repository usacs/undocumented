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
