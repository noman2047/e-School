from django.urls import path
from app_users import views


# app_name = 'app_users'
urlpatterns = [
    path('',views.HomeView.as_view(),name='index'),
    path('Schoolinfo/',views.Schoolinfo.as_view(),name='schoolinfo'),
    path('register/', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('teachers/', views.Teachers.as_view(), name="teachers"),
    path('calender/',views.Calender.as_view(),name='calender'),
    path('gaidlines/',views.Gaidlines.as_view(),name='gaidlines'),
    path('extracurricular/',views.Extracur.as_view(),name='extracur'),
    path('library/',views.Library.as_view(),name='library'),
    
]
