from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.template import Context
from django.template.loader import get_template
from django.shortcuts import render_to_response


def loginuser(request):
    """
    We might not need this, since django already provides a view for login at
    django.contrib.auth.views.login
    """
    if 'username' not in request.POST or 'password' not in request.POST:
        t = get_template('login.html')
        html = t.render(Context({}))
        return HttpResponse(html)

    username = request.POST['username']
    password = request.POST['password']
    
    if username == '' or password == '':
        return HttpResponse('please enter login')

    user = authenticate(username=username, password=password)
    if user is not None:
        return HttpResponse("correct!")
    else:
        return HttpResponse("incorrect!")


def test(request):
    d = {"foo":"bar"}
    return render_to_response("test.html", d)

