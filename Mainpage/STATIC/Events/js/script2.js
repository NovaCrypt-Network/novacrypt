// JavaScript Document
 $(document).ready(function() {
    $('#autoWidth2').lightSlider({
        autoWidth:true,
        loop:true,
        onSliderLoad: function() {
            $('#autoWidth2').removeClass('cS-hidden');
        } 
    });  
  });