# Django_todolist

Django App- todos

Database - mysql. Please refer settings.py for database configuration. For mysql setup, we need to install mysqlclient package. Below are
the steps to be followed:
1) sudo apt-get install python3-dev libmysqlclient-dev
2) pip install django mysqlclient

Connecting to the mysql database:

1) pip install mysql
2) systemctl status mysql.service
3) mysql -u <username> -p <password>
4) In the application folder, python migrate.py makemigrations <database_name>
5) python migrate.py migrate
5) python manage.py sqlmigrate <database_name> <table number from the previous step>
