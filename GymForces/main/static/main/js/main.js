$(document).ready(function(){
  var imgitems = $('.slider li').length;
  var imgpos = 1;

    for(i = 1; i<=imgitems; i++){
        $('.pagination').append(' <li><span class="fa fa-circle"></span></li>');
    }

    $('.slider li').hide();
    $('.slider li:first').show();
    $('.pagination li:first').css({'background': 'orange'});

    $('.pagination li').click(pagination);
    $('.right span').click(nextSlider);
    $('.left span').click(prevSlider);

    setInterval(function(){
        nextSlider();
    }, 4000);
    function pagination(){
      var paginationpos =  $(this).index() + 1;
      
        $('.slider li').hide();
        $('.slider li:nth-child('+ paginationpos +')').fadeIn();
   
        $('.pagination li').css({'background': 'orange'});
        $(this).css({'background': 'orange'});

        imgpos = paginationpos;
    }
    function nextSlider(){
        if(imgpos >= imgitems){
            imgpos = 1;
        }
        else{
            imgpos++;
      }

      $('.pagination li').css({'background': 'orange'});
        $('.pagination li:nth-child('+imgpos+')').css({'background': 'orange'});

        $('.slider li').hide();
        $('.slider li:nth-child('+imgpos+')').fadeIn();
   
    }

    function prevSlider(){
        if(imgpos <= 1){
            imgpos = imgitems;
        }
        else{
            imgpos--;
      }

      $('.pagination li').css({'background': 'orange'});
        $('.pagination li:nth-child('+imgpos+')').css({'background': 'orange'});

        $('.slider li').hide();
        $('.slider li:nth-child('+imgpos+')').fadeIn();
   
    }
});