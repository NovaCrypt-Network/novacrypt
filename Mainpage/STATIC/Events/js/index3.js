document.addEventListener("DOMContentLoaded", () =>{
    //Developed by Kanishk Kacholia
    //Initial setup to reduce redundancy
    const second = 1000,  
    minute = second * 60,
    hour = minute * 60,
    day = hour * 24;

    //Get event date from object
    EventTime = document.querySelector("#time-holder").dataset.time;
    countdown = new Date(EventTime).getTime();
    Interval = setInterval(function() {
        /* 
        Remember that the event date will not change, but normal time will.
        This will update the actual time and subtract accordingly.
        */
        now = new Date().getTime();
        distance = countdown - now;
        document.getElementById("days").innerText = Math.floor(distance / (day)),
        document.getElementById("hours").innerText = Math.floor((distance % (day)) / (hour)),
        document.getElementById("minutes").innerText = Math.floor((distance % (hour)) / (minute)),
        document.getElementById("seconds").innerText = Math.floor((distance % (minute)) / second);
        if (distance < 0) {
            let headline = document.getElementById("headline"),
                countdown = document.getElementById("countdown"),
                content = document.getElementById("content");
  
            headline.innerText = "It's my birthday!";
            countdown.style.display = "none";
            content.style.display = "block";
            clearInterval(Interval);
        }
    }, 0);
});