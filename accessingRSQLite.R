# test accessing a sqlite database using R
library("RSQLite")
drv <- dbDriver("SQLite")
conn <- dbConnect(drv,"/Users/joanneyeh/Dropbox/Datathon/cali_demographics_database.db")
dbListTables(conn)  # lists all tables in the database
dbListFields(conn, "t03w4f001") # lists all columns in a given table
dbListFields(conn,"codes")

dbDataType(conn, "columns")
dbDataType(conn, "vector_layers")
dbDataType(conn, "tables")
