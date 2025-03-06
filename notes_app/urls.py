from django.urls import path
from django.contrib.auth import views as auth_views
from .views import NoteListView, NoteCreateView, NoteUpdateView, NoteDeleteView, register

urlpatterns = [
    path('register/', register, name='register'),
    path("login/", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', NoteListView.as_view(), name='notes-list'),
    path('note/new/', NoteCreateView.as_view(), name='note-create'),
    path('note/<int:pk>/edit/', NoteUpdateView.as_view(), name='note-update'),
    path('note/<int:pk>/delete/', NoteDeleteView.as_view(), name='note-delete'),
]

