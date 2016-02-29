var mouth = $('<img id = "mouth" src = "/static/meals/images/mouthop.png">');
var gameOn = true;
var foodType = [ "F","P","C"];


$(function() {
  $('#gameWindow').append(mouth);
  play();
  $('body').on('keydown', function(e){    
    var pos = parseInt(mouth.css('margin-top'));    
    switch(e.which) {
    //up
    case 38:
      if (pos > 0){
        mouth.css('margin-top',(pos-100)+'px')
      }
      break;
    //down
    case 40: 
      if (pos < 200){
        mouth.css('margin-top',pos+100+'px')
      }
      break;
    }            
  })
});


function play() {  
  if (gameOn) {
    setTimeout(function(){    
      var food = $('<div>');
      render(food);            
      play();
      $.each ($('.lvl'), function(index,lvl){
        if ($(lvl).width() > 0 && $(lvl).width() < 100) {
          $(lvl).width($(lvl).width()-2);
        }else {
          $('#gameWindow').html("");          
          $('#gameWindow').append($('<h1>').text("Game Over"));
          var btn = $('<button>');
          btn.text('New Game');
          btn.attr('onClick', 'location.href=""');
          btn.addClass('btn');          
          $('#gameWindow').append(btn);
          gameOn = false;
        }
      });              
    }, 1000);    
  }    
};

function render(food) {

  var r = Math.floor(((Math.random() * 255) + 1));
  var g = Math.floor(((Math.random() * 255) + 1));
  var b = Math.floor(((Math.random() * 255) + 1));
  var color = 'rgb(' + r + ',' + g +',' + b + ')';
  food.css({background : color, marginTop : Math.floor(((Math.random() * 3)))*100 + 22 + 'px'});
  food.attr("data", foodType[Math.floor(Math.random() * 3)] );
  food.addClass('food');
  food.text(food.attr("data"));
  $('#gameWindow').append(food);
  food.animate(
    {
      marginLeft: "0px"
    },
    { 
      duration: ((Math.random() * 3) + 1)*500,
      progress: function() {if (!food.eaten) sense(food);},
      complete: function() {
        // Animation complete.
        if (food) food.remove();
      }
    }  
  );
}

function sense(food) {
  var pos = parseInt(food.css('margin-left')); 
  var ftop = parseInt(food.css('margin-top'))-22;
  var mtop = parseInt(mouth.css('margin-top'));     
  if ( pos < 105 && ftop == mtop ) {

    for (i=2; i<9; i++) {
      (function () {
        var j = i;
        setTimeout(function(){
          mouth.attr('src', "/static/meals/images/mouthop" + j + ".png");
          console.log(mouth.attr('src'));
        }, 100*j);
      }());    
    }     
    food.remove();
    food.eaten = true;
    var lvl = foodType.indexOf(food.attr("data")) + 1;
    var width = $('#lvl' + lvl).width();
    width = (width + 10 > 100) ?  100 :  width + 10 ;
    $('#lvl' + lvl).width(width); 
  }
}