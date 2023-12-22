<?php
 $host = 'Localhost';
 $user = 'root';
 $pass = '';
 $db = 'sample';

 $con = mysqli_connect($host, $user, $pass, $db);
 if($con)
    echo 'connected succesfully';
 $sql = "insert into smpl(username, password, email) values('jhon', 12345, 'a5@g.com)";
 $query = mysqli_query($con, $sql);
 if($query)
    echo 'data inserted succesfully';