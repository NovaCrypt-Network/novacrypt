var hasrun = false;
$(window).on("load resize scroll",function(){
    var windowTop = $(window).scrollTop(); //Distance from top of the page, increases as user scrolls down.
    if (hasrun == false && windowTop > 0){
        $('.count').each(function () {
            $(this).prop('Counter',0).animate({
                Counter: $(this).text()
            }, {
                duration: 4000,
                easing: 'swing',
                step: function (now) {
                    $(this).text(Math.ceil(now));
                }
            });
        });
        hasrun = true;
    }
});