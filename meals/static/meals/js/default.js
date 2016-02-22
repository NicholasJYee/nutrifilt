$(function() {
   
  $("#navBar ul li").on('click', function() {
    $(this).addClass('active').siblings('.active').removeClass('active');
    var cdiv = '#'+ $(this).children('.navText').text().toLowerCase();     
    $('#contents').children(cdiv).show().siblings().hide(); 
  });

  $('#loadForm').popup({ transition: 'all 0.3s'});

  $('#search').on('click', function(){
    $('#loadForm').load('/meals/search/');
  })

  $('body').on('click', '#test',function(){    
    $('.container').remove();
    var div = $('<div>');
    div.attr("class", "recipes");
    div.addClass("recipes");
    $('body').append(div);    
  })


});