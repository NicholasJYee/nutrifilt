$(function() {
       
  $("#navBar ul li").on('click', function() {
    $(this).addClass('active').siblings('.active').removeClass('active');
    var cdiv = '#'+ $(this).children('.navText').text().toLowerCase().replace(" ","");     
    $('.contents').children(cdiv).show().siblings().hide(); 
  });

  $('#loadForm').popup({ transition: 'all 0.3s'});
  $('#loadForm2').popup({ transition: 'all 0.3s'});

  $('#search').on('click', function(){
    $('#loadForm').load('/meals/search/', function() {
      $('#loadForm #id_name').attr('required',true);
      $('#loadForm #id_calories').attr('required',true);
      $('#loadForm p').slice(8).hide(); 

      var select_for_num_meals = $('#num_of_meals');
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

      $('#id_health_labels_12').prop('checked', true);

    });      
  });

  $('#search2').on('click', function(){
    $('#loadForm2').load('/meals/search2/', function() {
      $('#loadForm2 #age').attr('required',true);
      $('#loadForm2 #weight').attr('required',true);
      $('#loadForm2 #height').attr('required',true);
      $('#loadForm2 p').slice(6).hide(); 
      var select_for_num_meals = $('#num_of_meals2');
      meal_dropdown(select_for_num_meals);

      var rangeValues = {
        "1": "Meal cost: Cheapest",
        "5.5": "Meal cost: Cheap",
        "10": "Meal cost: Normal"
      };

      var rangeInput = $('#rangeInput2');
      var rangeText = $('#rangeText2');
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

  $('body').on('click', '#smart', function(){
    var cal = ($("#weight").val()*13.4) + ($("#height").val()*6.25) - ($("#age").val()*5);    
    if ($("#gender").val() == "1") {
      cal += 5;
      
    }else {
      cal -= 163;     
    }
    if ($("#planType").val() == "2") { cal -= 500};

    if ($("#planType").val() == "3") { cal += 5000};
    $("#id_calories").val(cal);
    $("#id_fat").val(cal*65/2000);
    $("#id_carbohydrates").val(cal*300/2000);
    if($("#planType").val() == "3") { 
      $("#id_protein").val(cal*50*1.3/2000);      
    } else {
      $("#id_protein").val(cal*50/2000);
    };    
  }); 

  $('body').on('submit', '.daForm',function(){   
    $('body').load("/meals/game");     
  }); 

  $('body').on('click','#chk', function(){
    if ($(this).text()=="Show more fields") {
      var num_input = 8 + parseInt($('select[name="num_of_meals"]').val());
      $('#loadForm p').slice(num_input).show();
      $(this).text("Hide extra fields");
    }else {
      var num_input = 8 + parseInt($('select[name="num_of_meals"]').val());
      $(this).text("Show more fields");  
      $('#loadForm p').slice(num_input).hide();
    }  
  });  
});

var meal_dropdown = function(select_for_num_meals) {
  if (select_for_num_meals.val() == 5) {
    var meal_dropdown_html =
      "<p class='meal-type'><select name=meal0>\n" +
      "  <option value='' disabled='disabled' selected='selected'>Select the type of meal</option>\n" +
      "  <option selected='selected' value='1'>Breakfast</option>\n" +
      "  <option value='2'>Snack</option>\n" +
      "  <option value='3'>Lunch</option>\n" +
      "  <option value='4'>Dinner</option>\n" +
      "</select></p>\n" +
      "<p class='meal-type'><select name=meal1>\n" +
      "  <option value='' disabled='disabled' selected='selected'>Select the type of meal</option>\n" +
      "  <option value='1'>Breakfast</option>\n" +
      "  <option selected='selected' value='2'>Snack</option>\n" +
      "  <option value='3'>Lunch</option>\n" +
      "  <option value='4'>Dinner</option>\n" +
      "</select></p>\n" +
      "<p class='meal-type'><select name=meal2>\n" +
      "  <option value='' disabled='disabled' selected='selected'>Select the type of meal</option>\n" +
      "  <option value='1'>Breakfast</option>\n" +
      "  <option value='2'>Snack</option>\n" +
      "  <option selected='selected' value='3'>Lunch</option>\n" +
      "  <option value='4'>Dinner</option>\n" +
      "</select></p>\n" +
      "<p class='meal-type'><select name=meal3>\n" +
      "  <option value='' disabled='disabled' selected='selected'>Select the type of meal</option>\n" +
      "  <option value='1'>Breakfast</option>\n" +
      "  <option selected='selected' value='2'>Snack</option>\n" +
      "  <option value='3'>Lunch</option>\n" +
      "  <option value='4'>Dinner</option>\n" +
      "</select></p>\n" +
      "<p class='meal-type'><select name=meal4>\n" +
      "  <option value='' disabled='disabled' selected='selected'>Select the type of meal</option>\n" +
      "  <option value='1'>Breakfast</option>\n" +
      "  <option value='2'>Snack</option>\n" +
      "  <option value='3'>Lunch</option>\n" +
      "  <option selected='selected' value='4'>Dinner</option>\n" +
      "</select></p>";
    $('.daForm > select').after(meal_dropdown_html);          
  } else {
    for (var i = select_for_num_meals.val() - 1; i >= 0; i--) {
      var meal_dropdown_html =
        "<select name=meal" + i + ">\n" +
        "  <option value='' disabled='disabled' selected='selected'>Select the type of meal</option>\n" +
        "  <option value='1'>Breakfast</option>\n" +
        "  <option value='2'>Snack</option>\n" +
        "  <option value='3'>Lunch</option>\n" +
        "  <option value='4'>Dinner</option>\n" +
        "</select>";
      $('.daForm > select').after("<p class='meal-type'>" + meal_dropdown_html + "</p>");
    }
  }
};