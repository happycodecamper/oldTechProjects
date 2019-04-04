//FCC_Random_Quote_Machine
// to Change Text with Click Events and Convert JSON Data to HTML
(function () {
  var quote = "";
  var author = "";
  $(document).ready(function () {
    $("#getNewQuote").on("click", function () {
      //$.getJSON("/json/quotes.json", function (json) {
      $.getJSON("https://raw.githubusercontent.com/happycodecamper/Random_Quotes/da76ab8e3b9c8f0278cd8e9b05a900ed8418ebe9/quotes.json", function (json) {
        var html = "";
        var randomQuote = json[Math.floor(Math.random() * json.length)];
        quote = randomQuote.quote;
        author = randomQuote.author;
        $(".quote").html(quote);
        $(".author").html(author);
        $("#tweet-quote").on("click", function () {
          window.open("http://twitter.com/intent/tweet?text=" + quote + " " + author);

        });// end tweet-quote
      }); //end getJson
    }); // end click
  }); //end function
})(); //IIFE
