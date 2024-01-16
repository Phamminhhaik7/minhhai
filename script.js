function toggleNavbar() {
  var navbar = document.getElementById("myNavbar");
  if (navbar.className === "navbar") {
    navbar.className += " responsive";
  } else {
    navbar.className = "navbar";
  }
}
  
  var list_name = [
      'Goblin no Suana 4 <br>👁️1.632.846',
      'Hatsukoi Jikan 2 <br>👁️695.840',
      'Hatsukoi Jikan 1 <br>👁️840.335',
      'Tsuma Netori Kan... <br>👁️460.800',
      'Sweet and Hot 1<br>👁️641.413',
      'Doukyo Suru Neneki 1 <br>👁️780.483',
      'Korashime 2 Kyouikuteki...<br>👁️2.445.601',
      'Aoharu Snatch 2 <br>👁️1.962.357',
      'Hatsukoi Jikan 1 <br>👁️840.335',
      'Kozukuri Bu 1 </b>👁️367.021',
      'Majo wa Kekkyoku Sono Kyaku to…<br>👁️2.156.424',
      'Mahou Touki Lilustear 1 <br>👁️570.249',
  ];
    for (var i = 0; i < list_name.length; i++) {
        var name_video = document.getElementById("name" + (i + 1));
        if (name_video) {
            name_video.innerHTML = list_name[i];
        }
    }
      
    var list_number_img = [
       'image/number/4.png',
       'image/number/2.png',
       'image/number/1.png',
       'image/number/1.png',
       'image/number/1.png',
       'image/number/1.png',
       'image/number/4.png',
       'image/number/2.png',
       'image/number/1.png',
       'image/number/1.png',
       'image/number/2.png',
       'image/number/1.png',
    ];
    for (var i = 0; i < list_number_img.length; i++) {
        var el = document.getElementById("number-img" + (i + 1));
        if (el) {
            el.src = list_number_img[i];
        }
    };
    
    
    var list_img = [
      "https://irex.cc/images/thumb/Goblin-no-Suana-4.jpg",
      "https://irex.cc/images/thumb/Hatsukoi-Jikan-2.jpg",
      "https://irex.cc/images/thumb/Hatsukoi-Jikan-1.jpg",
      "https://irex.cc/images/thumb/Tsuma-Netori-Kan-Bijutsu-Kyoushi-no-Baai-1.jpg",
      "https://irex.cc/images/thumb/Sweet-and-Hot-1.jpg",
      "https://irex.cc/images/thumb/Doukyo-Suru-Neneki-1.jpg",
      "https://irex.cc/images/thumb/Korashime-2-Kyouikuteki-Depaga-Shidou-4.jpg",
      "https://irex.cc/images/thumb/Aoharu-Snatch-2.jpg",
      "https://irex.cc/images/thumb/Mihitsu-no-Koi-1.jpg",
      "https://irex.cc/images/thumb/Kozukuri-Bu-1.jpg",
      "https://irex.cc/images/thumb/Majo-wa-Kekkyoku-Sono-Kyaku-to-The-Animation-2.jpg",
      "https://irex.cc/images/thumb/Mahou-Touki-Lilustear-1.jpg",
]
    for (var i = 0; i < list_img.length; i++) {
        var img = document.getElementById("img" + (i + 1));
        if (img) {
            img.src = list_img[i];
        }
    }
      
   var list_link = [
  'video/goblin_no_suana_4.php',
  'video/hatsukoi_jkan_2.php',
  'video/hatsukoi_jkan_1.php',
  'video/tsuma_netori_kan_1.php',
					'video/sweet_and_hot_1.php',
					'video/doukyo_suru_neneki_1.php',
					'video/korasime_2_kyouikuteki',
					'video/',
					'video/',
					'video/',
					'video/',
					'video/',
  ];
    for (var i = 0; i < list_link.length; i++) {
        var link = document.getElementById("a" + (i + 1));
        if (link) {
            link.href = list_link[i];
        }
    }

var list_3d_img = [
      'https://irex.cc/images/thumb/Opiumud-043-The-Beginning-The-Collapse-Of-The-Black-Castle-1.jpg',
      'https://irex.cc/images/thumb/Tifa-Rave-1.jpg',
      'https://1.bp.blogspot.com/-jWmNXu-uZZ4/XF7NBNKIVFI/AAAAAAAACl8/fDZP5XupaN85wsc3rczp4YdJO6yjTVnuACLcBGAs/w300/Rina-to-Ana.jpg',
      'https://irex.cc/images/thumb/yoshiwara%20Rose%20%E2%80%93%20Procession%20of%20Courtesans.jpg',
      'https://irex.cc/images/thumb/Netorinbo-epilogue.jpg ',
      'https://irex.cc/images/thumb/kaho-1.jpg ',
      'https://irex.cc/images/thumb/mikoto-1.jpg ',
      'https://irex.cc/images/thumb/Chiyoko-1.jpg ',
      'https://irex.cc/images/thumb/A-Night-in-Teyvat-Prank-Gone-Wrong-1.jpg ',
      'https://irex.cc/images/thumb/Opiumud-037-Honoka-Celebrity-true-love-fans.jpg ',
      'https://irex.cc/images/thumb/Discipline-back-alley.jpg ',
      'https://irex.cc/images/thumb/First-Assignment-Extended-Edition.jpg ',

]
    for (var i = 0; i < list_3d_img.length; i++) {
        var img3d = document.getElementById("img3d" + (i + 1));
        if (img3d) {
            img3d.src = list_3d_img[i];
        }
    }
      
      
      
      
   var list_3d_name = [
      'Kuroinu: The Beginning...<br>👁️</>846.075',
      'Tifa Rave 1<br>👁️1.464.458 ',
      'Rina to Ana 1<br>👁️1.973.817 ',
      'Yoshiwara Rose - Process...<br>👁️6.256.175',
      'Netorinbo Epilogue 1<br>👁️2.804.415',
      'Kaho (果穂) 1<br>👁️905.501',
      'Mikoto (美琴) 1<br>👁️784.226',
      'Chiyoko (智代子) 1<br>👁️1.226.243',
      'A Night in Teyvat Pra...<br>👁️1.381.046',
      'Opiumud-037 - Honoka Cel...<br>👁️1.924.791',
      'Discipline Back Alley<br>👁️760.204',
      'First Assignmen...<br>👁️1.149.431'
  ];
    for (var i = 0; i < list_3d_name.length; i++) {
        var name_3d_video = document.getElementById("name3d" + (i + 1));
        if (name_3d_video) {
            name_3d_video.innerHTML = list_3d_name[i];
        }
    }
      
      
    var list_3d_link = [
  'https://example.com',
  'https://example.com',
  'https://example.com',
  'https://example.com',
  ];
    for (var i = 0; i < list_3d_link.length; i++) {
        var link3d = document.getElementById("a3d" + (i + 1));
        if (link3d) {
            link3d.href = list_3d_link[i];
        }
    }
   var list_3d_number_img = [
       'image/number/1.png',
       'image/number/1.png',
       'image/number/1.png',
       'image/number/1.png',
       'image/number/1.png ',
       'image/number/1.png ',
       'image/number/1.png ',
       'image/number/1.png ',
       'image/number/1.png ',
       'image/number/1.png ',
       'image/number/1.png ',
       'image/number/1.png ',


];
    for (var i = 0; i < list_3d_number_img.length; i++) {
        var nm = document.getElementById("number-img3d" + (i + 1));
        if (nm) {
            nm.src = list_3d_number_img[i];
        }
    };

var list_kk_img = [
      'https://irex.cc/images/thumb/Opiumud-043-The-Beginning-The-Collapse-Of-The-Black-Castle-1.jpg',
      'https://irex.cc/images/thumb/Tifa-Rave-1.jpg',
      'https://1.bp.blogspot.com/-jWmNXu-uZZ4/XF7NBNKIVFI/AAAAAAAACl8/fDZP5XupaN85wsc3rczp4YdJO6yjTVnuACLcBGAs/w300/Rina-to-Ana.jpg',
      'https://irex.cc/images/thumb/yoshiwara%20Rose%20%E2%80%93%20Procession%20of%20Courtesans.jpg',
      'https://irex.cc/images/thumb/Netorinbo-epilogue.jpg ',
      'https://irex.cc/images/thumb/kaho-1.jpg ',
      'https://irex.cc/images/thumb/mikoto-1.jpg ',
      'https://irex.cc/images/thumb/Chiyoko-1.jpg ',
      'https://irex.cc/images/thumb/A-Night-in-Teyvat-Prank-Gone-Wrong-1.jpg ',
      'https://irex.cc/images/thumb/Opiumud-037-Honoka-Celebrity-true-love-fans.jpg ',
      'https://irex.cc/images/thumb/Discipline-back-alley.jpg ',
      'https://irex.cc/images/thumb/First-Assignment-Extended-Edition.jpg ',

]
    for (var i = 0; i < list_kk_img.length; i++) {
        var imgkk = document.getElementById("imgk" + (i + 1));
        if (imgkk) {
            imgkk.src = list_kk_img[i];
        }
    }
      
      
      
      
   var list_kk_name = [
      'Kuroinu: The Beginning...<br>👁️</>846.075',
      'Tifa Rave 1<br>👁️1.464.458 ',
      'Rina to Ana 1<br>👁️1.973.817 ',
      'Yoshiwara Rose - Process...<br>👁️6.256.175',
      'Netorinbo Epilogue 1<br>👁️2.804.415',
      'Kaho (果穂) 1<br>👁️905.501',
      'Mikoto (美琴) 1<br>👁️784.226',
      'Chiyoko (智代子) 1<br>👁️1.226.243',
      'A Night in Teyvat Pra...<br>👁️1.381.046',
      'Opiumud-037 - Honoka Cel...<br>👁️1.924.791',
      'Discipline Back Alley<br>👁️760.204',
      'First Assignmen...<br>👁️1.149.431'
  ];
    for (var i = 0; i < list_kk_name.length; i++) {
        var name_kk_video = document.getElementById("namek" + (i + 1));
        if (name_kk_video) {
            name_kk_video.innerHTML = list_kk_name[i];
        }
    }
      
      
    var list_kk_link = [
  'https://example.com',
  'https://example.com',
  'https://example.com',
  'https://example.com',
  ];
    for (var i = 0; i < list_kk_link.length; i++) {
        var linkkk = document.getElementById("ak" + (i + 1));
        if (linkkk) {
            link3d.href = list_kk_link[i];
        }
    }
   var list_kk_number_img = [
       'image/number/1.png',
       'image/number/1.png',
       'image/number/1.png',
       'image/number/1.png',
       'image/number/1.png',
       'image/number/1.png',
       'image/number/1.png',
       'image/number/1.png',
       'image/number/1.png',
       'image/number/1.png',
       'image/number/1.png',
       'image/number/1.png',


];
    for (var i = 0; i < list_kk_number_img.length; i++) {
        var nm = document.getElementById("number-imgk" + (i + 1));
        if (nm) {
            nm.src = list_kk_number_img[i];
        }
    };
    
    
    
 var link = location.href
document.getElementById('shareBtn').addEventListener('click', async () => {
  try {
    if (navigator.share) {
      await navigator.share({
   //     title: 'Your Website Title',
    //    text: 'Check out this website!',
        url: link,
      });
      console.log('Successfully shared');
    } else {
      console.log('Web Share API not supported');
    }
  } catch (error) {
    console.error('Error sharing:', error);
  }
});
var width = window.innerWidth || document.documentElement.clientWidth || document.body.clientWidth;
var height = window.innerHeight || document.documentElement.clientHeight || document.body.clientHeight;

// Đặt chiều rộng và chiều cao cho một phần tử bằng JavaScript
document.querySelector('.backgroundimg').style.width = width + 'px';
document.querySelector('.backgroundimg').style.height = height + 'px';