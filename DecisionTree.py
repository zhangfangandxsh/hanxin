
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
    <style>
        * {
            margin: 0;
            padding: 0;
        }

        div {
            width: 200px;
            height: 200px;
            background: pink;
            position: absolute;
            border-radius: 50%;
            top: 0;
            left: 0;
        }

        .box2 {
            width: 200px;
            height: 200px;
            background: skyblue;
            top: 200px;
            left: 200px;
        }
    </style>
</head>

<body>
    <div class="box1"></div>
    <div class="box2"></div>
</body>
<script>
    var box1 = document.querySelector(".box1");
    var box2 = document.querySelector(".box2");
    var cw = document.documentElement.clientWidth;
    var ch = document.documentElement.clientHeight;
    var bw = box1.offsetWidth;
    var bh = box1.offsetHeight;
    var movex = 0;
    var movey = 0;
    var movex2 = 300;
    var movey2 = 300;
    var speed = 1;
    var speedy = 1;
    var speed2 = 2;
    var speedy2 = 2;

    var sid = null;

    setInterval(function () {
        movex += speed;
        movex2 += speed2;
        movey += speedy;
        movey2 += speedy2;
        var x = movex + bw / 2 - box2.offsetLeft - box2.offsetWidth / 2;
        var y = movey + bw / 2 - box2.offsetTop - box2.offsetWidth / 2;
        var z = bw / 2 + box2.offsetWidth / 2;

        if (movex + bw >= cw) {
            speed = -speed;
        }
        if (movex < 0) {
            speed = -speed;
        }
        if (movey + bh >= ch) {
            speedy = -speedy;
        }
        if (movey < 0) {
            speedy = -speedy;
        }

        if (movex2 + box2.offsetWidth >= cw) {
            speed2 = -speed2;
        }
        if (movex2 < 0) {
            speed2 = -speed2;
        }
        if (movey2 + box2.offsetHeight >= ch) {
            speedy2 = -speedy2;
        }
        if (movey2 < 0) {
            speedy2 = -speedy2;
        }

        if (x * x + y * y < z * z) {
            if (!sid) {
                speed = -speed;
                speedy = -speedy;
                speed2 = -speed2;
                speedy2 = -speedy2;
                sid = setTimeout(function () {
                    sid = null;
                }, 1000);
            }
        }

        box1.style.left = movex + "px";
        box1.style.top = movey + "px";
        box2.style.left = movex2 + "px";
        box2.style.top = movey2 + "px";
    }, 1);
</script>

</html>
