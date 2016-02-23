$(function() {
   
  $("#navBar ul li").on('click', function() {
    $(this).addClass('active').siblings('.active').removeClass('active');
    var cdiv = '#'+ $(this).children('.navText').text().toLowerCase();     
    $('.contents').children(cdiv).show().siblings().hide(); 
  });

  $('#loadForm').popup({ transition: 'all 0.3s'});

  $('#search').on('click', function(){
    $('#loadForm').load('/meals/search/', function() {
      $('#loadForm p').slice(5).hide(); 
    });      
  });

  // testing results page
  $('body').on('click', '#test',function(){    
    $('.container').remove();
    var div = $('<div>');
    div.attr("class", "recipes");
    div.addClass("recipes");
    div.load('/meals/results'); 
    $('body').append(div);    
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