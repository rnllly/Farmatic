<!DOCTYPE html>
<html lang="{{ str_replace('_', '-', app()->getLocale()) }}">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">

        <title <?php echo $myname; ?>>3A</title>

        <style>
            body {
                font-family: 'Nunito', sans-serif;
            }
        </style>
    </head>
    <body class="antialiased">
        <center>
        <img src="<?php echo $mypic; ?>">
        <h1><?php echo $myname;?></h1>
        </center>
    </body>
</html>
