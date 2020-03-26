def set_session(request, obj=None):
    request.session.setdefault('username', obj.username)
    request.session.setdefault('nick_name', obj.nick_name)
    request.session.setdefault('user_uuid', str(obj.user_uuid))


def del_session(request, obj=None):
    del request.session['username']
    del request.session['nick_name']
    del request.session['user_uuid']