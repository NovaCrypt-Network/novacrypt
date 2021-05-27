from django.urls import path, re_path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

app_name = 'Administration'
urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('',views.login_request,name='login'),
    path('logout',views.logout_request,name='logout'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name = "Administration/reset_password.html", email_template_name = 'Administration/reset_password_email.html', success_url  = reverse_lazy('Administration:password_reset_done')), name ='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name = "Administration/password_reset_sent.html"), name ='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name = "Administration/password_reset_form.html", success_url  = reverse_lazy('Administration:password_reset_complete')), name ='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name = "Administration/password_reset_done.html"), name ='password_reset_complete'),
    path('change_password', views.change_password, name='change_password'),
    
    path('dashboard',views.dashboard,name="dashboard"),
    path('dashboard/external/<name>',views.profile_external,name="external_profile"),
    path('dashboard/profile',views.profile,name="profile"),
    path('dashboard/activity',views.activity,name="activity"),
    #path('dashboard/account',views.account,name="account"),
    #path('dashboard/blog',views.blog,name="blog"),
    #path('dashboard/event',views.event_manage,name="event"),
    #path('dashboard/event/<int:id_num>',views.event_editor,name="event_editor"),
]