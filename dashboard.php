<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>ADMIN</title>
  <link rel="stylesheet" href="styles.css"> 
    <style>
body {
background-color:yellow
}
</style>
</head>
<body>
<?php
session_start();
if (!isset($_SESSION['user_id'])) {
  echo 'CHƯA ĐĂNG NHẬP';
    // Chưa đăng nhập, chuyển hướng về trang đăng nhập
    header("Location: admin.php");
    exit();
}
echo 'HELO ADMIN';
echo "<button><a href ='?logout=True'</a>ĐĂNG XUẤT</button>";
if (isset($_GET['logout'])){
session_start();
session_destroy(); // Xóa tất cả các biến session
header("Location: admin.php");
exit();}
?>
<script src="script.js"defer>
</script>
</html>