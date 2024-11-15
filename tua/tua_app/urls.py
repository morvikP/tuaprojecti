from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.main, name="home"),
    path('valu', views.valu, name="valu"),
    path('stand', views.stand, name="stand"),
    path('deliv', views.deliv, name="deliv"),
    path('job', views.job, name="job"),
    path('disa', views.disa, name="disa"),
    path('cal', views.cal, name="cal"),
    path('good', views.good, name="good"),
    path('sign-up/', views.sign_up, name='sign_up'),
    path('login', views.login_page, name="login_page"),
    path('logout/', views.logout_view, name='logout_action'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)