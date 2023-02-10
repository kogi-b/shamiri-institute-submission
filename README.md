This script creates a Postgresql database and writes data contained in a csv file to the database. It is written to work on the localhost instance of a Postgresql database.

This script can be improved on by :

    Ingesting data in chunks, this is more suitable for cases where there is a lot of data to be ingested.

    Adding the capability to use different data sources and numerous databases.


There are different ways to achieve automation using the script depending on a given environment:

    On Windows, you can use the Task Scheduler to run the script whenever the CSV file is modified.

    In a cloud setup, the script can be set up to run using a lambda function

The above solutions would require modification of the script to suite the  environment in which it is used.