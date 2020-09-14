# Create Expense Call

I was able to create a MongoDB Atlas, connect to the DB and create a record by posting the request in Swagger UI. 

For the record id, I would retrieve the latest record id from the last updated record in the DB, increase by 1, and save it into a variable as the app starts to run. When the app needs to insert a record into DB, it would pack the record id into the dataframe, send it to DB and increase the value of id variable by 1.
