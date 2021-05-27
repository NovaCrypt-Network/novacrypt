$( document ).ready(function() {
    moment.updateLocale('en', {
        meridiem: function(hour, minute, isLowerCase) {
          if (hour < 12) {
            return 'a.m.';
          } else {
            return 'p.m.';
          }
        }
    });
    const csrftoken = Cookies.get('csrftoken');
    last_id = $(".ARTICLE_HOLDER").children().last().data("id");
    version_input = $(".ARTICLE_HOLDER").data("version");
    category_input = $(".ARTICLE_HOLDER").data("category");
    author_input = $(".ARTICLE_HOLDER").data("author");
    $(window).scroll(function() {
        if($(window).scrollTop() + $(window).height() == $(document).height()) {
            $(".loader").removeClass("d-none");
            $(".loader").addClass("d-block");
            $.ajax({
                url:"/Blog/ArticleAPI",
                type:"POST",
                data:{
                    'csrfmiddlewaretoken':csrftoken,
                    'version': version_input,
                    'category':category_input,
                    'author':author_input,
                    'id':last_id
                },
                dataType:'json',
                success : function(data){
                    $(".loader").removeClass("d-block");
                    $(".loader").addClass("d-none");
                    $.each(data.BlogObjects,function(key,val){
                        $(".ARTICLE_HOLDER").append(`
                        <div class="col-10 col-md-6 col-lg-4 mt-5 mt-lg-3 card d-flex special-card" style="width: 18rem;" data-id="${val.pk}">
                            <img class="card-img-top rounded" src="${val.thumbnail_url}" alt="${val.thumnail_desc}">
                            <div class="card-body">
                                <h5 class="card-title"><a class="article" href="/Blog/Article/${val.slug}">${val.title}</a></h5>
                                <p class="card-text text-muted">Posted by <a class="article" href="/Blog/Author/${val.username}">${val.first_name} ${val.last_name}</a> on ${moment(val.publish).format("MMM. D, YYYY, h:mm a")}</p>
                                <p class="card-text"><a class="article" href="/Blog/Category/${val.category}">${val.category}</a></p> 
                                <p class="card-text">${val.short_description}</p>
                            </div>
                        </div>
                        `)
                    })
                    last_id = $(".ARTICLE_HOLDER").children().last().data("id");
                },
            })
        }
     });
});