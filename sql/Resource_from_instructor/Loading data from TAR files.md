To load a database in Postgres, you can use PgAdmin, Command Prompt, or PSQL shell.

**PgAdmin:**

1. Configure PostgreSQL Binary path in Preferences.
1. Create a new database.
1. Right-click on the database and select "Restore."
1. Select the .tar file containing the database backup.
1. Click Restore to load the database.

**Command Prompt:**

1. Connect to the database using psql -U <username>.
1. Create a new database using create database \<database_name>.
1. Load the .tar file using psql -U <username> -d \<database_name> <file location>.

**PSQL Shell:**

1. Create a new database using create database \<database_name>.
1. Connect to the database using \\c \<database_name>.
1. Load the .tar file using \\i <file location>.# Loading data from TAR files.pdf (PDF file)
   ![Alt text](./Loading%20data%20from%20TAR%20files.pdf){ type=application/pdf style="min-height:100vh;width:100%" }
