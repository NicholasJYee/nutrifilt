$(function() { 
  $('body').on('mouseenter','.mealplan ul li img', function() {    
    $(this).closest('li').children('.nutable').show();      
  });
  $('body').on('mouseleave','.mealplan ul li img', function() {    
    $(this).closest('li').children('.nutable').hide();      
  });  
});

// function setHeight() {
//   console.log($('.ingredients').height());
//   console.log($('.mealplan').height());
//   if ($('.ingredients').height() < $('.mealplan').height()) {
//     $('.mealplan').height($('.ingredients').height());
//   } else {
//     $('.ingredients').height($('.mealplan').height());
//   }
// }
