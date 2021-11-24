$(document).ready(function () {
    $('#singup').submit(function (e) {
        e.preventDefault();
        let data = {
            'email': $(this).find('input[name="email"]').val(),
            'password': $(this).find('input[name="password"]').val(),
        }

        $.ajax({
            headers: {"X-CSRFToken": $('input[name="csrfmiddlewaretoken"]').val()},
            type: $(this).attr('method'),
            url: $(this).attr('url'),
            dataType: 'json',
            data: data,
            success: function (response) {
                alert('response');
                console.log(response)
                if(response == 'True') {
                    window.location.href = '/dashboard';
                } else {
                    alert(response);
                    return false;
                }
            }
        });
    });
});