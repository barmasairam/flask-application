#FIRST WE CREATED THE ONE CONTAINER FOR MYSQL USING THE BELOW COMMANDS
 docker pull mysql/mysql-server:tag
 docker run --name=mysql1 -d mysql/mysql-server:tag
 docker logs mysql1
 docker logs mysql1 2>&1 | grep GENERATED
 docker exec -it mysql1 mysql -uroot -p
 ALTER USER 'root'@'localhost' IDENTIFIED BY 'password';
 #AFTER THAT EXIT AND AGAIN LOGIN WITH MYSQL
 docker exec -it mysql1 mysql -uroot -p
 #HERER PASSWORD IS PASSWORD
 #AFTER THAT CREATE DATABASE BY USING THESR COMMANDS
 CREATE DATABASE MyDB;
 USE MyDB;
 CREATE TABLE MyUsers ( firstname VARCHAR(30) NOT NULL,  lastname VARCHAR(30) NOT NULL);
 #AFTER THAT CREATE USER BY USING THE FOLLOWING COMMANDS
 CREATE USER 'db_user'@'%' IDENTIFIED BY 'XXXXXXXXXXXX';
 GRANT ALL PRIVILEGES ON MyDB.* TO 'db_user'@'%';
 FLUSH PRIVILEGES;
 CREATE USER 'root'@'%' IDENTIFIED BY 'PASSWORD';
 GRANT ALL PRIVILEGES ON . TO 'root'@'%' WITH GRANT OPTION;
 FLUSH PRIVILEGES;
#UP TO HERE MYSQL CONTAINER IS DONE.
#NOW YOU HAVE TO BUILD THE CONTAINER FOR FLASK BY USING THESE COMMANDS
move to flask-application directory then use these commands here we are also linking the two containers
docker build -t flask .
docker run -it  -p 5000:5000  --name=flaskapp --link mysql1 -d flask
#after you access this page you will get the success.
