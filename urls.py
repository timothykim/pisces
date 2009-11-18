from django.conf.urls.defaults import *

urlpatterns = patterns('brochure.views',
    #root
    (r'^$', 'welcome'),
)




urlpatterns += patterns('',
    (r'^i18n/', include('django.conf.urls.i18n')),

    #accounts
    (r'^accounts/login$', 'django.contrib.auth.views.login',
        {'template_name': 'login.html'}),

    # Pattern below will never fire in test or production server
    # It's here only for development environment
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': 'static'}),
)
