# Tasks completed

- Create Expense

Because of the time limit, I only finished one function. I was able to create a MongoDB Atlas, connect to the DB and create a record by posting the request in Swagger UI. From the data parameters checking, I did not implement it in backend since I reckon it could be done in frontend. For the record id, I would retrieve the latest record id from the last updated record in the DB, increment bt 1, and save it into a variable as the app starts to run. When the app needs to insert a record into DB, it would pack the record id into the data frame, send it to DB and increment bt 1.
