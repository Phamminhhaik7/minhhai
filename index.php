<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>HENTA.IO</title>
  <link rel="stylesheet" href="styles.css"> 
</head>
<body>
<main>
  <?php
    include('reuse/navbar.php');
    ?>
<div style="position:relative;display:flex;margin-top:20px">
 <p class="text">HENTAI MỚI</p>
 <p class="rounded-text">TẤT CẢ</p>
</div>
<?php
include ('database.php');
$sql="SELECT * FROM `NewVideo` ORDER BY `Stt` DESC"; 
$stagement=$conn -> query($sql);
$stagement -> execute();
$data =$stagement -> fetchAll(PDO::FETCH_ASSOC);
print_r ($data);

$Stt = $data[0]['Stt'];
$Name = array();
$View = array();
$Link = array();
$LinkBanner = array();
$Eposides = array();
for ($i = 1; $i <= $Stt; $i++) {
    $Name_one = $data[$i - 1]['Name'];
    array_push($Name, $Name_one);
    $Link_one = $data[$i - 1]['Link'];
    array_push($Link, $Link_one);
    $LinkBanner_one = $data[$i - 1]['LinkBanner'];
    array_push($LinkBanner, $LinkBanner_one);
    $Eposides_one = $data[$i - 1]['Eposides'];
    array_push($Eposides, $Eposides_one);
    $View_one = $data[$i - 1]['View'];
    array_push($View, $View_one);
};



$element_count = 12;
echo '<div class="container ">';
for ($i = 1; $i <= $element_count; $i++) {
    echo '<div class="image-container">';
    echo '<a href="'.$Link[$i-1].'">';
    echo '<img  class="img-post" src="'.$LinkBanner[$i-1].'">';
    echo '<div class="overlay-rectangle">'.$Name[$i-1].' '.$Eposides[$i-1].'<br>👁️'.$View[$i-1].'</div>';
    echo '<img class="number" src="image/number/'.$Eposides[$i-1].'.png">';
    echo '</a>';
    echo '</div>';
}
echo '</div>';
?>
<div style="position:relative;top:5px;display:flex;margin:0">
<p class="text">HENTAI 3D</p>
<p class="rounded-text">TẤT CẢ</p>
</div>
  <!--3d-->
 <?php

$element_count = 12;
echo '<div class="container ">';
for ($i = 1; $i <= $element_count; $i++) {
    echo '<div class="image-container">';
    echo '<a id="a3d' . $i . '" href="#">';
    echo '<img id="img3d' . $i . '" class="img-post" src="#">';
    echo '<div id="name3d' . $i . '" class="overlay-rectangle">#text</div>';
    echo '<img id="number-img3d' . $i . '" class="number" src="#">';
    echo '</a>';
    echo '</div>';
}
echo '</div>';
?>

  <!--Không che-->
<div style="position:relative;top:5px;display:flex;margin:0">
<p class="text">KHÔNG CHE</p>
<p class="rounded-text">TẤT CẢ</p>
</div>
<?php

$element_count = 12;
echo '<div class="container ">';
for ($i = 1; $i <= $element_count; $i++) {
    echo '<div class="image-container">';
    echo '<a id="ak' . $i . '" href="#">';
    echo '<img id="imgk' . $i . '" class="img-post" src="#">';
    echo '<div id="namek' . $i . '" class="overlay-rectangle">#text</div>';
    echo '<img id="number-imgk' . $i . '" class="number" src="#">';
    echo '</a>';
    echo '</div>';
}
echo '</div>';
?>

  
</main>
<footer >
  <?php
    include('reuse/end.php');
    ?>
</footer>
<script src="script.js"defer>
</script>
</body>
</html>