$(document).ready(function () {
    $('#singin').submit(function (e) {
        e.preventDefault();
        let data = {
            'fio': $(this).find('input[name="fio"]').val(),
            'email': $(this).find('input[name="email"]').val(),
            'password': $(this).find('input[name="password"]').val(),
        }

        $.ajax({
            headers: {"X-CSRFToken": $('input[name="csrfmiddlewaretoken"]').val()},
            type: $(this).attr('method'),
            url: $(this).attr('url'),
            data: data,
            success: function (response) {
                if(response == 'True') {
                    window.location.href="/dashboard";
                } else {
                    alert(response);
                    return false;
                }
            }
        });
    });
});