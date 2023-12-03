from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_page, name='index'),
    path('profile', views.profile_page, name='profile'),
    path('blogs', views.blogs_page, name='blogs'),
    path('portfolio', views.portfolio_page, name='portfolio'),
    path('contact-me', views.contact_me_page, name='contact-me'),
    path('review', views.review_page, name='review'),
    path('thankyou', views.thankyou_page, name='thankyou'),
    path('success', views.success_page, name='success'),
    path('search/', views.search_results, name='search_results'),
]
