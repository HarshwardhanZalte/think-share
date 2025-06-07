from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('home/', views.home, name='home'),
    path('createpost/', views.createpost, name='createpost'),
    path('<int:post_id>/edit/', views.editpost, name='editpost'),
    path('<int:post_id>/delete/', views.deletepost, name='deletepost'),
    path('accounts/logout/', views.logout1, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


