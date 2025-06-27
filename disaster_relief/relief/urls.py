from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('report/', views.report_disaster, name='report_disaster'),
    path('disasters/', views.disaster_list, name='disaster_list'),
    path('first_donation/',views.first_donation,name='first_donation'),
    path('', views.home, name='home'),
    path('article/<int:article_id>/', views.article_detail, name='article_detail'),
     path('news/', views.news_view, name='news'),
     path('contact/', views.contact, name='contact'),
path('about/',views.about,name='about'),
path('index/',views.index,name='index'),
path('process-payment/', views.process_payment, name='process_payment'),
    path("donation/", views.donation, name="donation"),
    path('thank-you/', views.thank_you, name='thank_you'),  # Add this line
    path("volunteer_signup/", views.volunteer_signup, name="volunteer_signup"),
    path("Thanks/",views.Thanks,name='Thanks'),


    path('report_missing_person/', views.report_missing_person, name='report_missing_person'),
    path('missing-persons_list/', views.missing_persons_list, name='missing_persons_list'),
    





]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


   
