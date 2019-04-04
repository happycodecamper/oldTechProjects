// run JQuery
$(document).ready(function() {
  // when search is clicked the code runs
  $('#search').click(function(){
    // gets search input
    var searchTerm = $('#searchTerm').val();
    // API URL with search input searchTerm
    //var url = 'https://en.wikipedia.org/w/api.php?action=opensearch&search=' + searchTerm + '&limit=1&namespace=0&format=json&callback=?';
    var url = 'https://en.wikipedia.org/w/api.php?action=opensearch&search=' + searchTerm + '&format=json&callback=?';

    $.ajax({
      type:'GET',
      url:url,
      async:false,
      dataType:'json',
      success: function (data) {
        //// get heading console.log(data[1][0]); title
        //console.log("data 1, title: " + data[1][0]);
        //// get heading console.log(data[2][0]); description
        //console.log("data 2, description: " + data[2][0]);
        //// get heading console.log(data[3][0]); wikipedia
        //console.log("data 3, wikipedia: " + data[3][0]);

        //console.log("data stringify:" + JSON.stringify(data));
        //console.log("data:" + data);
        //console.log(data[0][1]);

        //$("#output").prepend(data[1][0]);

        $("#output").html(''); // clear previous search
        for (var i = 0; i < data[1].length; i++) {
          //$("#output").prepend("<li><a target='_blank' href= " + data[3][i] + ">" + data[1][i] + " </a><p>" + data[2][i] + "</p></li>");
          $("#output").prepend("<li><a target='_blank' class='pretty' href= " + data[3][i] + ">" + data[1][i] + " </a><p>" + data[2][i] + "</p></li>");

        }
        $("#searchTerm").val('');  // empty the search box
      },
      error: function(errorMessage){
        alert("Error");
      }
    });
  });
  $("#searchTerm").keypress(function(e) {
  if(e.which==13) {
    $("#search").click();
  }
  });
});