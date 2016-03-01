$(function() {
       
  $("#navBar ul li").on('click', function() {
    $(this).addClass('active').siblings('.active').removeClass('active');
    var cdiv = '#'+ $(this).children('.navText').text().toLowerCase();     
    $('.contents').children(cdiv).show().siblings().hide(); 
  });

  $('#loadForm').popup({ transition: 'all 0.3s'});

  $('#search').on('click', function(){
    $('#loadForm').load('/meals/search/', function() {
      $('#loadForm input:lt(4)').attr('required',true);
      $('#loadForm input').slice(3).attr('pattern','\d+');
      $('#loadForm p').slice(6).hide(); 

      var select_for_num_meals = $('select[name="num_of_meals"]');
      meal_dropdown(select_for_num_meals);

      var rangeValues = {
        "1": "Meal cost: Cheapest",
        "5.5": "Meal cost: Cheap",
        "10": "Meal cost: Normal"
      };

      var rangeInput = $('#rangeInput');
      var rangeText = $('#rangeText');
      rangeText.text(rangeValues[rangeInput.val()]);
      rangeInput.on('input change', function () {
        rangeText.text(rangeValues[$(this).val()]);
        console.log(rangeValues[$(this).val()])
      });

      select_for_num_meals.change(function() {
        $('.meal-type').remove();
        meal_dropdown(select_for_num_meals);
      });

    });      
  });

  $('body').on('submit', '#daForm',function(){   
    $('body').load("/meals/game");     
  }); 

  $('body').on('click','#chk', function(){
    if ($(this).text()=="Show more fields") {
      var num_input = 5 + parseInt($('select[name="num_of_meals"]').val());
      $('#loadForm p').slice(num_input).show();
      $(this).text("Hide extra fields");
    }else {
      var num_input = 5 + parseInt($('select[name="num_of_meals"]').val());
      $(this).text("Show more fields");  
      $('#loadForm p').slice(num_input).hide();
    }  
  });  
});

var meal_dropdown = function(select_for_num_meals) {
  if (select_for_num_meals.val() == 5) {
    var meal_dropdown_html =
      "<p class='meal-type'><select name=meal0>\n" +
      "  <option value='' disabled='disabled' selected='selected'>Please select the type of meal</option>\n" +
      "  <option selected='selected' value='1'>Breakfast</option>\n" +
      "  <option value='2'>Snack</option>\n" +
      "  <option value='3'>Lunch</option>\n" +
      "  <option value='4'>Dinner</option>\n" +
      "</select></p>\n" +
      "<p class='meal-type'><select name=meal1>\n" +
      "  <option value='' disabled='disabled' selected='selected'>Please select the type of meal</option>\n" +
      "  <option value='1'>Breakfast</option>\n" +
      "  <option selected='selected' value='2'>Snack</option>\n" +
      "  <option value='3'>Lunch</option>\n" +
      "  <option value='4'>Dinner</option>\n" +
      "</select></p>\n" +
      "<p class='meal-type'><select name=meal2>\n" +
      "  <option value='' disabled='disabled' selected='selected'>Please select the type of meal</option>\n" +
      "  <option value='1'>Breakfast</option>\n" +
      "  <option value='2'>Snack</option>\n" +
      "  <option selected='selected' value='3'>Lunch</option>\n" +
      "  <option value='4'>Dinner</option>\n" +
      "</select></p>\n" +
      "<p class='meal-type'><select name=meal3>\n" +
      "  <option value='' disabled='disabled' selected='selected'>Please select the type of meal</option>\n" +
      "  <option value='1'>Breakfast</option>\n" +
      "  <option selected='selected' value='2'>Snack</option>\n" +
      "  <option value='3'>Lunch</option>\n" +
      "  <option value='4'>Dinner</option>\n" +
      "</select></p>\n" +
      "<p class='meal-type'><select name=meal4>\n" +
      "  <option value='' disabled='disabled' selected='selected'>Please select the type of meal</option>\n" +
      "  <option value='1'>Breakfast</option>\n" +
      "  <option value='2'>Snack</option>\n" +
      "  <option value='3'>Lunch</option>\n" +
      "  <option selected='selected' value='4'>Dinner</option>\n" +
      "</select></p>";
    $('#daForm > select').after(meal_dropdown_html);          
  } else {
    for (var i = select_for_num_meals.val() - 1; i >= 0; i--) {
      var meal_dropdown_html =
        "<select name=meal" + i + ">\n" +
        "  <option value='' disabled='disabled' selected='selected'>Please select the type of meal</option>\n" +
        "  <option value='1'>Breakfast</option>\n" +
        "  <option value='2'>Snack</option>\n" +
        "  <option value='3'>Lunch</option>\n" +
        "  <option value='4'>Dinner</option>\n" +
        "</select>";
      $('#daForm > select').after("<p class='meal-type'>" + meal_dropdown_html + "</p>");
    }
  }
};