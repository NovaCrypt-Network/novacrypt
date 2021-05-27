$( document ).ready(function() {
    const csrftoken = Cookies.get('csrftoken');
    $(".selectpicker.Country").change(function(){
        $.ajax({
            url:"/community/CountryAPI",
            type:"POST",
            data:{
                'csrfmiddlewaretoken':csrftoken,
                'CountryID': $(this).val(),
            },
            dataType:'json',
            success : function(data){
                $('.selectpicker.Chapter').prop('disabled', false);
                $('.selectpicker.Chapter').empty();
                $.each(data,function(key,val){
                    $('.selectpicker.Chapter').append(`<option value="${val.pk}">${val.fields.reigon}: ${val.fields.name}</option>`);
                })
                $('.selectpicker.Chapter').selectpicker('refresh');
            },
        })
    })
    $(".selectpicker.Chapter").change(function(){
        $.ajax({
            url:"/community/ChapterAPI",
            type:"POST",
            data:{
                'csrfmiddlewaretoken':csrftoken,
                'ChapterID': $(this).val(),
            },
            dataType:'json',
            success : function(data){
                $(".DISPLAY").empty();
                console.log(data);
                $(".DISPLAY").append(`
                    <h1 data-aos="fade-left">${data.name}</h1>
                    <h3 data-aos="fade-left">${data.reigon}, ${data.country}</h3>
                    <h5 data-aos="fade-left">President: ${data.name}</h5>
                    <h5 data-aos="fade-left">Email: <a href="mailto:${data.email}">${data.email}</a></h5>
                `);
                if(data.website !== undefined){
                    $(".DISPLAY").append(`<h5 data-aos="fade-left"><a href="${data.website}">Website</a></h5>`);
                }
                if(data.instagram !== undefined){
                    $(".DISPLAY").append(`<h5 data-aos="fade-left"><a href="${data.instagram}">Website</a></h5>`);
                }
            },
        })
    })
});