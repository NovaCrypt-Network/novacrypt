$(document).ready(function () {
    const csrftoken = Cookies.get('csrftoken');
    $(".Name_Counter").text(`Letters Remaining: ${($(".Name_Field").attr('maxLength') - $(".Name_Field").val().length)}`);
    $(".Short_Counter").text(`Letters Remaining: ${($(".Short_Field").attr('maxLength') - $(".Short_Field").val().length)}`);
    $(".Name_Field").keydown(function (e) { 
        $(".Name_Counter").text(`Letters Remaining: ${($(".Name_Field").attr('maxLength') - $(".Name_Field").val().length)}`);
    });
    $(".Short_Field").keydown(function (e) { 
        $(".Short_Counter").text(`Letters Remaining: ${($(".Short_Field").attr('maxLength') - $(".Short_Field").val().length)}`);
    });
    $(".FAQ_Delete").click(function (e) {
        var ClickItem = $(this);
        $.ajax({
            type: "POST",
            url: "/Administration/dashboard/event/FAQDelete",
            data: {
                'csrfmiddlewaretoken':csrftoken,
                'FAQ_ID':$(this).attr('id')
            },
            dataType: "json",
            success: function (response) {
                ClickItem.parent().parent().parent().remove();
            }
        });
    });
    $(".FAQ_Submit").click(function (e) { 
        question = $("#id_question").val();
        answer = $("#id_answer").val();
        EVENT_ID = $(this).attr('id');
        $.ajax({
            type: "POST",
            url: "/Administration/dashboard/event/FAQCreate",
            data: {
                'csrfmiddlewaretoken':csrftoken,
                'question':question,
                'answer':answer,
                'event':EVENT_ID
            },
            dataType: "json",
            success: function (response) {
                newItem = $(`
                <div class="app-card alert alert-dismissible shadow-sm border-left-decoration" role="alert">
                    <div class="inner">
                        <div class="app-card-body p-3 p-lg-4">
                            <h3 class="mb-3">${response.question}</h3>
                            <div class="row gx-5 gy-3">
                                <div class="col-12 col-lg-9">
                                    <div>${response.answer}</div>
                                </div>
                                <div class="col-12 col-lg-3">
                                </div>
                            </div>
                            <button type="button" class="btn-close" aria-label="Close" id="${response.id}"></button>
                        </div>
                    </div>
                </div>
                `).insertBefore('#FAQ_Adder');
                newItem.click(function (e) {
                    $.ajax({
                        type: "POST",
                        url: "/Administration/dashboard/event/FAQDelete",
                        data: {
                            'csrfmiddlewaretoken':csrftoken,
                            'FAQ_ID':response.id
                        },
                        dataType: "json",
                        success: function (response) {
                            newItem.remove();
                        }
                    });
                });
                question = $("#id_question").val('');
                answer = $("#id_answer").val('');
            }
        });
    });
});