from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.template import Context
from django.template.loader import get_template

def loginuser(request):
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

