from django.urls import path
from . import views

urlpatterns = [
    path('', views.AquaFaze, name="home-page"),
    path('AquaFaze', views.AquaFaze, name="home-page"),
    path('login', views.loginpage, name="login_page"),
    path('signup',views.signuppage,name="signup_page"),
    path('aboutus', views.aboutus, name="about_us"),
    path('detailed',views.detailed,name="detailed_analysis"),
    path('activito', views.activito, name="activito"),
    path('blogs', views.blogs, name="read_blogs"),

    path('buisness',views.buisness,name="buisness"),
    path('logout', views.logout_view, name='logout'),
    path('my_account', views.my_account, name='account'),
    path('quick', views.quick, name='quick_analysis'),
    path('process_image', views.process_image, name='profile'),
    path('show_result', views.show_result, name='show_result'),
    path('feedback', views.feedback, name='feedback_form'),

    path('profile', views.profile, name='profile'),
    path('update', views.update, name='profile'),
    path('activity', views.activity, name='profile'),
    path('activity#section', views.activity_section, name='profile'),
    path('error', views.error, name='error'),
    path('error404', views.error404, name='error'),

    # path('send_otp', views.send_otp, name='send_otp')
    # path('map', views.map, name='profile'),

]
