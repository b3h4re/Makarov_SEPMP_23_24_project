from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_view
from django.urls import path

from mipt_first_year.base import views as base_view
from mipt_first_year.room import views as room_view
from mipt_first_year.room.views import list_rooms
from mipt_first_year.student.views import user_page
from mipt_first_year.student.views import start_chat
from mipt_first_year.users import views as users_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', base_view.home, name="home"),
    path('register/', users_view.register, name="register"),
    path('login/', auth_view.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('password-reset/', auth_view.PasswordResetView.as_view(
        template_name='password_reset.html'), name='password_reset'),
    path('password-reset/done', auth_view.PasswordResetDoneView.as_view(
        template_name='password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>', auth_view.PasswordResetConfirmView.as_view(
        template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('profile/', users_view.profile, name="profile"),
    # path("user/<str:username>/", user_page, name="user_page"),
    path("user/<int:user_id>/", user_page, name="user_page"),
    path("start-chat/<int:student_id>/<int:user_id>", start_chat, name="start_chat"),
    path("user/<int:user_id>/rooms", list_rooms, name="list_rooms"),
    path('room/<slug:slug>/', room_view.room, name='room'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)