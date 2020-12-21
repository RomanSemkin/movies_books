<html>
<head>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
    <style>
        body {
            padding-top: 40px;
            padding-bottom: 40px;
            background-color: #ADABAB;
        }
        .form-signin {
            max-width: 330px;
            padding: 15px;
            margin: 0 auto;
            color: #017572;
        }
        .form-signin .form-control {
            position: relative;
            height: auto;
            -webkit-box-sizing: border-box;
            -moz-box-sizing: border-box;
            box-sizing: border-box;
            padding: 10px;
            font-size: 16px;
        }

        .form-signin .form-control:focus {
            z-index: 2;
        }

        .form-signin input[type="password"] {
            margin-bottom: 10px;
            border-top-left-radius: 0;
            border-top-right-radius: 0;
            border-color: #017572;
        }
        h2 {
            text-align: center;
            color: #017572;
        }
    </style>
</head>
<body>
<h2>Enter book ISBN</h2>
<div class="container form-signin">
    <form form class = "form-signin" role = "form" method="POST" action="">
        <input type = "text" class = "form-control"
               name = "jwt_token" placeholder = "Token"
               required autofocus></br>
        <input type = "text" class = "form-control"
               name = "title" placeholder = "Title"
               required ></br>
        <input type = "text" class = "form-control"
               name = "year" placeholder = "Year"
               ></br>
        <input type = "text" class = "form-control"
               name = "plot" placeholder = "Plot"
               ></br>
        <button class = "btn btn-md btn-primary btn-block " type = "submit"
                name = "submit">Send</button>
    </form>
</div>

<div class = "container form-group" >
    <?php
    if (isset($_POST["submit"])) {
        $handle = curl_init();
        $token = $_POST["jwt_token"];
        $title = $_POST["title"];

        $params = array('title' => $title);
        $url = $_ENV["API_HOST"].":".$_ENV["API_PORT"]."/api/v1/movie/". '?' . http_build_query($params);
        $headers = [
            'Authorization: Bearer '.$token,
            'Content-Type: multipart/form-data;',
        ];

        curl_setopt($handle, CURLOPT_URL, $url);
        curl_setopt($handle, CURLOPT_CUSTOMREQUEST, "GET");
        curl_setopt($handle, CURLOPT_RETURNTRANSFER, true);
        curl_setopt($handle, CURLOPT_HTTPHEADER, $headers);

        $data = curl_exec($handle);
        if (curl_errno($handle)) {
            print curl_error($handle);
        }
        curl_close($handle);
        print "<textarea class='form-control' rows='5'>".$data."</textarea>";
    }
    ?>
</div> <!-- /container -->
</body>
</html>
