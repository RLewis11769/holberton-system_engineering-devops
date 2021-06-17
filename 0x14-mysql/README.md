# MySQL

## 0
- Make sure public key is in ~/.ssh/authorized_keys in both web01 and web02
    - sudo apt-get install mysql-server
    - ALWAYS set password for MySQL

## 1
- Create user for both web01 and web02
    - Grant replication client privileges to user
        - CREATE USER holberton_user@localhost IDENTIFIED BY 'projectcorrection280hbtn';
        - GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';

## 2
- Create database, table, and values in web01
    - Grant select privileges to user created in task 1
        - CREATE DATABASE tyrell_corp;
        - USE tyrell_corp
        - CREATE TABLE nexus6 (ID INT NOT NULL AUTO_INCREMENT,
                               NAME VARCHAR(256)
                               PRIMARY KEY(ID));
        - INSERT INTO nexus6 (NAME) VALUES ("Vader");
        - SELECT * FROM nexus6;
        - GRANT SELECT ON *.* to 'holberton_user'@'localhost';

## 3
- Create replica user on web01
    - Grant replication secondary privileges to replica user
    - Grant select privileges on mysql.user to user created in task 1 (so can see permissions)
        - CREATE USER 'replica_user'@'%' IDENTIFIED BY 'replica_pw';
        - GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%';
        - GRANT SELECT ON mysql.user TO 'holberton_user'@'localhost';
        - SELECT user, Repl_slave_priv FROM mysql.user;

## 4
- Update config files for primary/replica
    - In /etc/mysql/mysql.conf.d/mysqld.cnf:
        - bind_address
        - server-id
        - log_bin
        - binlog_do_db
    - See:
        - 4-mysql_configuration_primary
            - Config file for web01
        - 4-mysql_configuration_replica
            - Config file for web02
- Set up primary/replica connection in web02
    - In primary:
        - sudo ufw allow 3306 (this is default port for MySQL for firewall)
        - mysqldump -uroot -p tyrell_corp > dump.sql
            - This creates dump file that should be copied into replica
        - SHOW MASTER STATUS;
            - Keep note of:
                - File (to be used as MASTER_LOG_FILE)
                - Position (to be used as MASTER_LOG_POS)
    - In replica:
        - CREATE DATABASE tyrell_corp;
        - mysql -uroot -p tyrell_corp < dump.sql
            - This makes an identical copy of database from primary in replica
            - dump.sql is copy-pasted into file but could use scp command
        - STOP SLAVE;
        - CHANGE MASTER TO
            - MASTER_HOST='54.174.125.120', (primary's IP address)
            - MASTER_USER='replica_user', (replica's username)
            - MASTER_PASSWORD='replica_pw', (replica's password)
            - MASTER_LOG_FILE='mysql-bin.000002', (primary's File status)
            - MASTER_LOG_POS=613; (primary's Position status)
        - START SLAVE;
        - service mysql restart
    - Test with:
        - In primary:
            - USE tyrell_corp
            - INSERT INTO nexus6 (NAME) VALUES ("Shadow");
            - SELECT * FROM nexus6;
        - In replica:
            - SELECT * FROM nexus6;
                - Should be identical to database in primary!
            - SHOW SLAVE STATUS\G
                - Slave_IO_State: Waiting for master to send event
    