$("[data-trigger]").on("click", function(){
    var trigger_id =  $(this).attr('data-trigger');
    $(trigger_id).toggleClass("show");
    $('body').toggleClass("offcanvas-active");
});

// close button 
$(".btn-close").click(function(e){
    $(".navbar-collapse").removeClass("show");
    $("body").removeClass("offcanvas-active");
}); 

$(window).on("load resize scroll",function(){
    var windowTop = $(window).scrollTop(); //Distance from top of the page, increases as user scrolls down.
    var elementTop = $(".stat-holder").offset().top; //Constant as to where an object's y position on the screen is.
    var Bounds = windowTop - elementTop; //Negative at first but as the element goes above the user's screen it becomes positive
    if (Bounds >= 0){
        $(".navbar").css({"background-color":"#1d1e1f"});
    }
    else{
        $(".navbar").css({"background-color":"transparent"});
    }
});