
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">

    <!-- Custom CSS -->
    <link rel="stylesheet" href="{{ url_for('static', filename='css/custom.css') }}">

    <!-- basic navbar [DELETE IF NOT USEFUL] -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
      <div class="container">
        <a class="navbar-brand" href="/">FastFlask</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarsExample07" aria-controls="navbarsExample07" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>

        <div class="collapse navbar-collapse" id="navbarsExample07">
          <ul class="navbar-nav mr-auto">
            <li class="nav-item active">
              <a class="nav-link" href="/">Index</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="/admin">Admin</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">Another</a>
            </li>
            <li class="nav-item dropdown">
              <a class="nav-link dropdown-toggle" href="https://example.com" id="dropdown07" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">DropMenu</a>
              <div class="dropdown-menu" aria-labelledby="dropdown07">
                <a class="dropdown-item" href="#">Put</a>
                <a class="dropdown-item" href="#">Links</a>
                <a class="dropdown-item" href="#">Here</a>
              </div>
            </li>
          </ul>
          <form class="form-inline my-2 my-md-0">
            <a href="/login" type="button" class="btn btn-warning">Login</a>
            <a href="/register" type="button" class="btn btn-info" style="margin-left: 10px;">Register</a>
          </form>
        </div>
      </div>
    </nav>

    <!-- Block Head -->
    {% block head %} 
    <!-- title tag is inside the 'block head' in child html's -->
    {% endblock %}

  </head>
  <body>
    {% block body %} 
    <!-- title tag is inside the 'block head' in child html's -->


        {% block content %}

        {% endblock %}

    {% endblock %}



    <div class="container">
    
        <!-- DELETE BELOW THIS LINE-->
        <br>
    <div class="jumbotron">
      <h1 class="display-4">If you can read this, you are up to go!</h1>
      <p class="lead">I hope this save you some time! </p>
      <hr class="my-4">
      <p>If you like this, please follow me on github <a style="color: red; text-decoration: none;" href="https://github.com/ngeorgj">@ngeorgj</a></p>
      <p>In case of bugs, compliments or comments email to <b>ngj.netrunner@gmail.com</b></p>
      <p class="lead">
        <a class="btn btn-primary btn-lg" href="#" role="button">Enjoy</a>
      </p>
    </div>
        <!-- END DELETE HERE -->
        
    </div>

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->

    <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
    <script src="{{ url_for('static', filename='js/custom.js') }}">
  </body>
</html>    
        
