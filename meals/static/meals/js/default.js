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
    });      
  });

  $('body').on('submit', '#daForm',function(){
    $(this).append('<img src = "/static/meals/images/load.gif">');
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