from django.shortcuts import render_to_response
from django.utils.translation import ugettext as _


def welcome(request):
    context = {
        'LANGUAGES' : (
                        ('en', _('English')),
                        ('ko', _('Korean')),
                        ),
    }
    
    return render_to_response("welcome.html", context)


