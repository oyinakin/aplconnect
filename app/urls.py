from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls import url, include
from django.views.static import serve

urlpatterns = [
    path('', views.home, name ='home'),
    path('signin', views.signin, name ='signin'),
    path('signout', views.signout, name ='signout'),
    path('contact-us', views.contact, name ='contact'),	
    path('dashboard', views.dashboard, name ='dashboard'),
    path('save_task', views.save_task, name ='save_task'),
    path('edit_task', views.edit_task, name ='edit_task'),
    path('retrieve_task', views.retrieve_task, name ='retrieve_task'),	
    path('add_message', views.add_message, name ='add_message'),
    path('retrieve_message', views.retrieve_message, name ='retrieve_message'),
    path('change_password', views.change_password, name ='change_password'),
    path('update_message', views.update_message, name ='update_message'),
    path('check_session_validity', views.check_session_validity, name ='check_session_validity'),
    path('password_reset',auth_views.PasswordResetView.as_view(template_name='password_reset_form.html'),name='password_reset',),
    path('password_reset/done',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name='password_reset_done',),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),name='password_reset_confirm',),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name='password_reset_complete',),
        
]