<?php
/* Database credentials. Assuming you are running MySQL
server with default setting (user 'root' with no password) */
const _HOST ='localhost';
const _USER = 'root';
const _PASS= '';
const _DB= 'newpage';
 
 $dsn ='mysql:dbname='._DB.';host='._HOST;
/* Attempt to connect to MySQL database */
$conn = new PDO($dsn,_USER,_PASS);
// Check connection




?>
  