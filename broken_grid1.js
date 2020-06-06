function myFunction(x) {
  if (x.matches) { // If media query matches
    $('#switch1').empty();
     $('#switch1').append('<div class="col-lg-6 d-flex justify-content-center position-relative"><div class="display-box2"><h4 class="d-title ">Expand on your projects</h4><hr><p class="d-text">Have a project you are already working on? Use it in the networking hub! Meet professionals of different skills such as web design, video editing, photo editing, and business to help you with your needs!</p></div></div>', '<div class="col-lg-6 col-md-12 col-sm-12 d-flex justify-content-center"><div class="img-box2"></div></div>'); 
    
    $('#switch2').empty();
     $('#switch2').append('<div class="col-lg-6 d-flex justify-content-center position-relative"><div class="display-box4"><h4 class="d-title ">Spark and share new ideas</h4><hr><p class="d-text">Want to discover leaders in your area? Join your local chapter and meet the people who are doing great things in your community! Or create your own chapter!</p></div></div>', ' <div class="col-lg-6 col-md-12 col-sm-12 d-flex justify-content-center"><div class="img-box4 right-box"></div></div>'); 
      $('#switch3').empty();
     $('#switch3').append('<div class="col-lg-6 d-flex justify-content-center position-relative"><div class="display-box6"><h4 class="d-title ">Find New Opportunities</h4><hr><p class="d-text">We have a bot featured in our server that scrapes job/team postings from other servers like StudentPort and NovaCrypt! There you can find new ideas, teams, and businesses currently looking for people like you! In addition, our website holds an archive of grants, internship opportunities, lab spaces, and programs you can apply to, along with a matching system for people looking for recruitment!</p></div></div>','<div class="col-lg-6 col-md-12 col-sm-12 d-flex justify-content-center"><div class="img-box6 right-box"></div></div>');
      
      
}else{
    $('#switch1').empty();
    $('#switch1').append('<div class="col-lg-6 col-md-12 col-sm-12 d-flex justify-content-center"><div class="img-box2"></div></div>','<div class="col-lg-6 d-flex justify-content-center position-relative"><div class="display-box2 right-box"><h4 class="d-title ">Expand on your projects</h4><hr><p class="d-text">Have a project you are already working on? Use it in the networking hub! Meet professionals of different skills such as web design, video editing, photo editing, and business to help you with your needs!</p></div></div>'); 
    
    $('#switch2').empty();
     $('#switch2').append('<div class="col-lg-6 col-md-12 col-sm-12 d-flex justify-content-center"><div class="img-box4"></div></div><div class="col-lg-6 d-flex justify-content-center position-relative"><div class="display-box4 right-box"><h4 class="d-title ">Spark and share new ideas</h4><hr><p class="d-text">Want to discover leaders in your area? Join your local chapter and meet the people who are doing great things in your community! Or create your own chapter!</p></div></div>'); 
    
    $('#switch3').empty();
     $('#switch3').append('<div class="col-lg-6 col-md-12 col-sm-12 d-flex justify-content-center"><div class="img-box6"></div></div><div class="col-lg-6 d-flex justify-content-center position-relative"><div class="display-box6 right-box"><h4 class="d-title ">Find New Opportunities</h4><hr><p class="d-text">We have a bot featured in our server that scrapes job/team postings from other servers like StudentPort and NovaCrypt! There you can find new ideas, teams, and businesses currently looking for people like you! In addition, our website holds an archive of grants, internship opportunities, lab spaces, and programs you can apply to, along with a matching system for people looking for recruitment!</p></div></div>');
}
}
var x = window.matchMedia("(max-width: 991px)")
myFunction(x) // Call listener function at run time
x.addListener(myFunction) // Attach listener function on state changes