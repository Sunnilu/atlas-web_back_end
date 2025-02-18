Enter password: 
bob@dylan:~$ 
bob@dylan:~$ mysql -uroot -p holberton
Enter password: 
mysql> SELECT COUNT(name) FROM names WHERE name LIKE 'a%';
+-------------+
| COUNT(name) |
+-------------+
|      302936 |
+-------------+
1 row in set (2.19 sec)
mysql> 
mysql> exit
bye