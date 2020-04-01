def auth(request):
    """
    Return context variables required by apps that use Django's authentication
    system.

    If there is no 'user' attribute in the request, use AnonymousUser (from
    django.contrib.auth).
    """
    if hasattr(request, 'blog_user'):
        blog_user = request.blog_user
    else:
        from django.contrib.auth.models import AnonymousUser
        blog_user = AnonymousUser()

    return {
        'blog_user': blog_user,
    }
