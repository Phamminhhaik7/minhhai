<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>THE LOAI</title>
  <link rel="stylesheet" href="styles.css"> 
</head>
<body>
  <?php
  include("reuse/navbar.php");  
  ?>
  <?php
$element_count = 12;
echo '<div class="container ">';
for ($i = 1; $i <= $element_count; $i++) {
    echo '<div class="image-container">';
    echo '<a id="a' . $i . '" href="#">';
    echo '<img id="img' . $i . '" class="img-post" src="#">';
    echo '<div id="name' . $i . '" class="overlay-rectangle">#text</div>';
    echo '<img id="number-img' . $i . '" class="number" src="#">';
    echo '</a>';
    echo '</div>';
}
echo '</div>'
?>
 <?php
 include 'reuse/end.php'
 ?>
<script src="script.js"defer>
</script>
</body>
</html>