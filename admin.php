<?php
session_start(); // Bắt đầu session
include 'database.php'; // Kết nối đến cơ sở dữ liệu
if (isset($_SESSION['user_id'])) {
    // Chưa đăng nhập, chuyển hướng về trang đăng nhập
    header("Location: dashboard.php");
    exit();
}
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Nếu form được gửi đi

    $user = $_POST['username'];
    $pass = $_POST['password'];

    // Kiểm tra tài khoản và mật khẩu
    $sql = "SELECT * FROM `admin_account`;";
    $stagement=$conn -> query($sql);
    $stagement -> execute();
    $data =$stagement -> fetchAll(PDO::FETCH_ASSOC);
    
    $dbpass= $data[0]['password'];
    $dbuser = $data[0]['username'];
    if  (password_verify($pass,$dbpass) && $user==$dbuser){
        
        
        $_SESSION['user_id'] = $dbpass; // Lưu thông tin người dùng vào session
        header("Location: dashboard.php"); // Chuyển hướng đến trang dashboard hoặc trang chính của ứng dụng
        exit();
    } else {
        // Đăng nhập thất bại, hiển thị thông báo
        $error_message = 'Sai mật khẩu hoặc tài khoản. Vui lòng thử lại.';
    }
}

?>

<!DOCTYPE html>
<html lang="en">
  <head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>ADMIN</title>
  <link rel="stylesheet" href="styles.css"> 
    <style>
body{
background-image:url('a.jpg');
background-size: 100%;
    background-repeat:repeat;
    background-attachment: fixed;
}
input[type="text"] {
    width: auto; 
    margin :0;
    height:50%;
    padding: 5px; 
    border: 5px solid #ccc; 
    border-radius: 5px; 
    outline: none; 
}
input[type="submit"] {
    width: auto; 
    margin :5px;
    height:50%;
    border: 5px solid cyan; 
    border-radius: 5px; 
    outline: none; 
    background-color:cyan;
    font-weight:bold
}
h3{
  margin :1px;
}

    
input[type="text"]:focus {
    background-color: #f0f0f0;
}

</style>
</head>

<body>
  
    <form class='box_in_text' style='display:block;margin:0 auto;text-align:center;width:300px;height :fit-content;position :relative  ;top:50px;background-color:rgb(225,225,225,0.5);color:white ' method='post' action="admin.php">
        <h1>LOGIN</h1>
        <h3>User</h3> <input type="text" name="username" placeholer='Tài khoản' />
        <h3>Password:</h3> <input type="text" name='password' plackeholer='Mật khẩu' /><br>
        <input type="submit" value="Đăng nhập" /><br>
    

    <?php
    if (isset($error_message)) {
        echo '<p style="color: red;">' . $error_message . '</p>';
    }
    ?>
  </form>
</body>
</html>