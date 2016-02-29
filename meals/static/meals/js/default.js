$(function() {
   
  $("#navBar ul li").on('click', function() {
    $(this).addClass('active').siblings('.active').removeClass('active');
    var cdiv = '#'+ $(this).children('.navText').text().toLowerCase();     
    $('.contents').children(cdiv).show().siblings().hide(); 
  });

  $('#loadForm').popup({ transition: 'all 0.3s'});

  $('#search').on('click', function(){
    $('#loadForm').load('/meals/search/', function() {
      $('#loadForm input:lt(3)').attr('required',true);
      $('#loadForm input').slice(2).attr('pattern','\d+');
      $('#loadForm p').slice(5).hide(); 

      // Nick's jQuery
      var select_for_num_meals = $('select[name="num_of_meals"]')
      select_for_num_meals.change(function() {
        for (var i = select_for_num_meals.val() - 1; i >= 0; i--) {
          var meal_dropdown =
            "<select name=meal" + i + ">\n" +
            "  <option value='' disabled='disabled' selected='selected'>Please select the type of meal</option>\n" +
            "  <option value='1'>Breakfast</option>\n" +
            "  <option value='2'>Snack</option>\n" +
            "  <option value='3'>Lunch</option>\n" +
            "  <option value='4'>Dinner</option>\n" +
            "</select>"
          $('#daForm > select').after("<p>" + meal_dropdown + "</p>")  
        }
      });
    });      
  });

  $('body').on('submit', '#daForm',function(){
    // $(this).append('<img src = "/static/meals/images/load.gif">');
    $(this).hmtl('');
    $(this).load('/meals/game');
  }); 

  $('body').on('click','#chk', function(){
    if ($(this).text()=="Show more fields") {
      $('#loadForm p').slice(5).show();
      $(this).text("Hide extra fields");
    }else {
      $(this).text("Show more fields");  
      $('#loadForm p').slice(5).hide();
    }  
  });
});