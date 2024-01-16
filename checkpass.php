<?php
  session_start();
  if (isset($_SESSION['user_id'])) {
    // Chưa đăng nhập, chuyển hướng về trang đăng nhập
    header("Location: dashboard.php");
    exit();
}

  if (isset($_POST['username'],$_POST['password'])){
    include 'database.php';
    $user=$_POST['username'];
    $pass=$_POST['password'];
    $sql = "SELECT * FROM `admin_account`;";
    $stagement=$conn -> query($sql);
    $stagement -> execute();
    $data =$stagement -> fetchAll(PDO::FETCH_ASSOC);
    print_r ($data)
    $dbpass= $data[0]['password'];
    $dbuser = $data[0]['username'];
    if  (password_verify($pass,$dbpass) and $user==$dbuser){
        echo 'Đăng nhập thành công';
        session_start();
        $_SESSION['user_id'] = $dbpass; // Lưu ID người dùng hoặc thông tin khác
        echo $_SESSION;
        header("Location: dashboard.php"); // Chuyển hướng đến trang dashboard hoặc trang chính của ứng dụng
        exit();
    }
    elseif (!isset($_POST['username'],$_POST['password'])){}
    else{
      echo 'Sai mật khẩu hoặc tài khoản vui lòng nhập lại';
      header("Location:admin.php?success=false");
    }}*\
   
  ?>