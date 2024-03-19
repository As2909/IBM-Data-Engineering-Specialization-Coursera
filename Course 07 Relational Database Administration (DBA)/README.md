## Project Description
For this project you will assume the role of database administrator at a data analytics consulting company. You have been assigned to a project where you need to setup, test and optimize the data platform. The platform contains different on premises database servers like MySQL, PostgreSQL, and cloud-based databases like IBM DB2. Your job is to configure, tune, secure, backup and monitor those databases and keep them running at peak performance.

This is a three-part assignment.

- [Part 1](https://github.com/As2909/IBM-Data-Engineering-Specialization-Coursera/blob/main/Course%2007%20Relational%20Database%20Administration%20(DBA)/week%204/Part1.pdf): You will work with PostgreSQL server and perform the User Management tasks and handle the backup of the databases.

- [Part 2](https://github.com/As2909/IBM-Data-Engineering-Specialization-Coursera/blob/main/Course%2007%20Relational%20Database%20Administration%20(DBA)/week%204/Part2.pdf): You will work with MySQL server and perform the tasks like configuration check, recovery of data. You will use indexing to improve the database performance. You will identify which storage engines are supported by the server and which table uses which storage engine. Optionally you will also automate backup tasks.

- [Part 3](https://github.com/As2909/IBM-Data-Engineering-Specialization-Coursera/blob/main/Course%2007%20Relational%20Database%20Administration%20(DBA)/week%204/Part3.pdf): You will work with the cloud instance of IBM DB2 server and perform the tasks like restoration of data, index creation to improve the query performance. You will create views to make queries easier to write. Optionally you will also connect to the cloud instance of IBM DB2 server and from command line.

## Tasks and Solutions
- Task 1.1 - Find the settings in PostgreSQL (1 pts)\
![alt text](https://github.com/As2909/IBM-Data-Engineering-Specialization-Coursera/blob/main/Course%2007%20Relational%20Database%20Administration%20(DBA)/week%204/max-connections.png)

- Task 1.2 - Create an User (1 pts)\
![alt text](https://github.com/As2909/IBM-Data-Engineering-Specialization-Coursera/blob/main/Course%2007%20Relational%20Database%20Administration%20(DBA)/week%204/create-user.png)

- Task 1.3 - Create a Role (1 pts)\
![alt text](https://github.com/As2909/IBM-Data-Engineering-Specialization-Coursera/blob/main/Course%2007%20Relational%20Database%20Administration%20(DBA)/week%204/create-role.png)

- Task 1.4 - Grant privileges to the role (2 pts)\
![alt text](https://github.com/As2909/IBM-Data-Engineering-Specialization-Coursera/blob/main/Course%2007%20Relational%20Database%20Administration%20(DBA)/week%204/grant-privs-to-role.png)

- Task 1.5 - Grant role to an user (1 pts)\
![alt text](https://github.com/As2909/IBM-Data-Engineering-Specialization-Coursera/blob/main/Course%2007%20Relational%20Database%20Administration%20(DBA)/week%204/grant-role.png)

- Task 1.6 - Backup a database on PostgreSQL server (1 pts)\
![alt text](https://github.com/As2909/IBM-Data-Engineering-Specialization-Coursera/blob/main/Course%2007%20Relational%20Database%20Administration%20(DBA)/week%204/backup-database.png)

- Task 2.1 - Restore MySQL server using a previous backup (1 pts)\
![alt text](https://github.com/As2909/IBM-Data-Engineering-Specialization-Coursera/blob/main/Course%2007%20Relational%20Database%20Administration%20(DBA)/week%204/database-restore.png)

- Task 2.2 - Find the table data size (1 pts)\
For this task, we can use the SELECT function to query the size of the database from information_schema.tables or using the show table status\
![alt text](https://github.com/As2909/IBM-Data-Engineering-Specialization-Coursera/blob/main/Course%2007%20Relational%20Database%20Administration%20(DBA)/week%204/table-data-size.png)

- Task 2.3 - Baseline query performance (1 pts)\
![alt text](https://github.com/As2909/IBM-Data-Engineering-Specialization-Coursera/blob/main/Course%2007%20Relational%20Database%20Administration%20(DBA)/week%204/query-base-line.png)

- Task 2.4 - Create an index. (1 pts)\
![alt text](https://github.com/As2909/IBM-Data-Engineering-Specialization-Coursera/blob/main/Course%2007%20Relational%20Database%20Administration%20(DBA)/week%204/index-creation.png)

- Task 2.5 - Document the improvement in query performance. (1 pts)\
![alt text](https://github.com/As2909/IBM-Data-Engineering-Specialization-Coursera/blob/main/Course%2007%20Relational%20Database%20Administration%20(DBA)/week%204/query-indexed.png)

- Task 2.6 - Find supported storage engines (1 pts)\
![alt text](https://github.com/As2909/IBM-Data-Engineering-Specialization-Coursera/blob/main/Course%2007%20Relational%20Database%20Administration%20(DBA)/week%204/storage-engines.png)

- Task 2.7 - Find the storage engine of a table (1 pts)\
![alt text](https://github.com/As2909/IBM-Data-Engineering-Specialization-Coursera/blob/main/Course%2007%20Relational%20Database%20Administration%20(DBA)/week%204/storage-engine-type.png)

- Task 3.1 - Restore the table billing. (2 pts)\
![alt text](https://github.com/As2909/IBM-Data-Engineering-Specialization-Coursera/blob/main/Course%2007%20Relational%20Database%20Administration%20(DBA)/week%204/restore-table.png)

- Task 3.2 - Create a view named basicbilldetails with the columns customerid, month, billedamount. (1 pts)\
![alt text](https://github.com/As2909/IBM-Data-Engineering-Specialization-Coursera/blob/main/Course%2007%20Relational%20Database%20Administration%20(DBA)/week%204/create-view.png)

- Task 3.3 - Baseline query performance. (1 pts)\
![alt text](https://github.com/As2909/IBM-Data-Engineering-Specialization-Coursera/blob/main/Course%2007%20Relational%20Database%20Administration%20(DBA)/week%204/query-baseline-db2.png)

- Task 3.4 - Create an index. (1 pts)\
![alt text](https://github.com/As2909/IBM-Data-Engineering-Specialization-Coursera/blob/main/Course%2007%20Relational%20Database%20Administration%20(DBA)/week%204/index-creation-db2.png)

- Task 3.5 - Document the improvement in query performance. (1 pts)\
![alt text](https://github.com/As2909/IBM-Data-Engineering-Specialization-Coursera/blob/main/Course%2007%20Relational%20Database%20Administration%20(DBA)/week%204/query-after-index.png)
