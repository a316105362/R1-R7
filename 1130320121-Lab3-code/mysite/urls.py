from django.conf.urls import *
from addr_book.views import *
import addr_book

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    (r'^$', addr_book.views.first),
    (r'^glance/$', addr_book.views.glance),
    (r'^glance/detail.*/$', addr_book.views.detail),
    (r'^glance/delete.*/$', addr_book.views.delete),
    (r'^glance/update.*/$', addr_book.views.update),
    (r'^glance/upda_author.*/$', addr_book.views.update_author),
    (r'^new_author1/$', addr_book.views.new_author1),
    (r'^insert/$', addr_book.views.insert),
    (r'^insert_author/$', addr_book.views.insert_author),
    (r'^new_author/$', addr_book.views.new_author),
    (r'^search_form/$', addr_book.views.search_form),
    (r'^search/$', addr_book.views.search),
)
