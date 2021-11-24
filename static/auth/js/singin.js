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
                if (response == 'True') {
                    window.location.href = "/dashboard";
                } else {
                    let r = JSON.parse(response);
                    console.log(r);
                    $('.form-error').show();
                    $('.form-error').empty();

                    if (r['email']) {
                        r['email'].forEach(function (item) {
                            $('.form-error').append(
                                "<label>" + item['message'] + "</label>"
                            );
                        });
                    }
                    if (r['password_repeat']) {
                        r['password_repeat'].forEach(function (item) {
                            $('.form-error').append(
                                "<label>" + item['message'] + "</label>"
                            );
                        });
                    }
                    if (r['fio']) {
                        r['fio'].forEach(function (item) {
                            $('.form-error').append(
                                "<label>" + item['message'] + "</label>"
                            );
                        });
                    }
                    if (r['password']) {
                        r['password'].forEach(function (item) {
                            $('.form-error').append(
                                "<label>" + item['message'] + "</label>"
                            );
                        });
                    }
                }
            }
        });
    });
});