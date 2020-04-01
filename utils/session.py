def set_session(request, obj=None):
    request.session.setdefault('user_uuid', str(obj.user_uuid))


def del_session(request, obj=None):
    del request.session['user_uuid']