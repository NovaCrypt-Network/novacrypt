$(document).ready(function() {

/* Every time the window is scrolled ... */

$(window).scroll( function(){

/* Check the location of each desired element */
$('.fade-in-from-left').each( function(i){

    var bottom_of_object = $(this).position().top + $(this).outerHeight();
    var bottom_of_window = $(window).scrollTop() + $(window).height();


    /* If the object is completely visible in the window, fade it it */
    if( bottom_of_window > bottom_of_object ){

        $(this).removeClass('hidden');
        $(this).addClass('fade-in-from-left');
    }    else {
            $(this).addClass('hidden');
               }

});
$('.fade-in-from-right').each( function(i){

    var bottom_of_object = $(this).position().top + $(this).outerHeight();
    var bottom_of_window = $(window).scrollTop() + $(window).height();


    /* If the object is completely visible in the window, fade it it */
    if( bottom_of_window > bottom_of_object ){

        $(this).removeClass('hidden');
        $(this).addClass('fade-in-from-right');
    }    else {
            $(this).addClass('hidden');
               }

}); 
}); 
});