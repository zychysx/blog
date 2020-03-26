$(function () {
    $('#login_btn').click(function () {
        var username = $('#username').val()
		var password = $('#password').val()
		var csrfmiddleware = $("input[name='csrfmiddlewaretoken']").val()

		var params =  {
			'username':username,
			'password':password,
			'csrfmiddlewaretoken':csrfmiddleware,
		}
		$.post('/user/login/',params,function (data) {
				if (data.status == 1) {
					location.reload()
				} else {
					$('.login_prompt').text(data.msg)

				}
			}
		)
    })
})