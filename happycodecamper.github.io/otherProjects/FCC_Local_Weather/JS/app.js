$(document).ready(function () {
  //This function gets temperature in Kelvin and returns Fahrenheit
  //to calculate temp in Fahrenheit and Celsius
  //To display Fahrenheit unit  -> &#8457;
  //To display Celsius unit  -> &#8451;
  function getTemp(temp) {
    var Fahrenheit;
    var Celsius;
    var Kelvin;
    var tempUnit = true;

    Kelvin = temp;

    Fahrenheit = ((Kelvin) * (9 / 5) - 459.67).toFixed(1);

    Celsius = (Kelvin - 273).toFixed(1);

    $("#Fahrenheit").html(Fahrenheit + " &#8457;"); //defaults temp in Fahrenheit
    //to toggle between Fahrenheit and Celsius
    $("#Fahrenheit").click(function () {
      if (tempUnit === false) {
        $("#Fahrenheit").html(Fahrenheit + " &#8457;");
        tempUnit = true;
      } else {
        $("#Fahrenheit").html(Celsius + " &#8451;");
        tempUnit = false;
      }
    });
    return Fahrenheit;
  }

  function changeBgd(Fahrenheit) {
    //to change background according to the temp
    if (Fahrenheit >= 90) {
      $("html")
      .css({
        //'background-image': 'url(../img/bay_Bridge.jpg)',
        'background-image': 'url(https://raw.githubusercontent.com/happycodecamper/FCC_Local_Weather_1/master/FCC_Local_Weather/img/bay_Bridge.jpg)',
        'background-repeat': 'no-repeat',
        'background-attachment': 'fixed',
        'background-size': 'cover'
      });
    } else if (Fahrenheit >= 60 && Fahrenheit < 90) {
      $("html")
      .css({
        //'background-image': 'url(../img/canyon_River.jpg)',
        'background-image': 'url(https://raw.githubusercontent.com/happycodecamper/FCC_Local_Weather_1/master/FCC_Local_Weather/img/canyon_River.jpg)',
        'background-repeat': 'no-repeat',
        'background-attachment': 'fixed',
        'background-size': 'cover'
      });
    } else {
      $("html")
     .css({
       //'background-image': 'url(../img/Switzerland_Mountains.jpg)',
       'background-image': 'url(https://raw.githubusercontent.com/happycodecamper/FCC_Local_Weather_1/master/FCC_Local_Weather/img/Switzerland_Mountains.jpg)',  
       'background-repeat': 'no-repeat',
       'background-attachment': 'fixed',
       'background-size': 'cover'
     });
    }
  }

  //Default is Kelvin. Options are imperial for Fahrenheit or metric for Celsius
  var units = "imperial";
  var long;
  var lat;

  // Get Geolocation Data 
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(function (position) {
      long = position.coords.longitude;
      lat = position.coords.latitude;

      $("#data").html("latitude: " + lat + "<br>longitude: " + long);

      //weather API with units variable
      //var api = 'http://api.openweathermap.org/data/2.5/weather?lat=' + lat + '&lon=' + long + "&units=" + units + '&appid=e2db5b0453a25a492e87ad8b03046a7c';

      //weather API without units variable that returns temp in Kelvin
      var api = 'https://api.openweathermap.org/data/2.5/weather?lat=' + lat + '&lon=' + long + '&appid=e2db5b0453a25a492e87ad8b03046a7c';

      $.getJSON(api, function (data) {
        var Fahrenheit = getTemp(data.main.temp);
        changeBgd(Fahrenheit);
        //changeBgd(60);

        //JSON call for Open Weather API
        var weather = data.weather[0].description;
        var windSpeed = data.wind.speed;
        var city = data.name;

        $("#city").html(city);
        $("#weather").html(weather);

        windSpeed = (2.237 * (windSpeed)).toFixed(1);
        $("#windSpeed").html(windSpeed + " mph");
      });
    }, function (failure) {
      console.log("location failure");
      changeBgd(91);//default
    });//end navigator
  }//end if
});