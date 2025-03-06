from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Note
from .forms import NoteForm

@login_required
def home(request):
    return render(request, 'home.html')

from django.contrib.auth.mixins import LoginRequiredMixin

class NoteListView(LoginRequiredMixin, ListView):
    model = Note
    template_name = 'notes_list.html'
    context_object_name = 'notes'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Note.objects.filter(user=self.request.user)
        return Note.objects.none()  # Return an empty queryset if not logged in


class NoteCreateView(CreateView):
    model = Note
    form_class = NoteForm
    template_name = 'notes_app/note_form.html'
    success_url = reverse_lazy('notes-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

from django.views.generic import UpdateView
from django.urls import reverse_lazy
from .models import Note

class NoteUpdateView(UpdateView):
    model = Note
    fields = ['title', 'content']
    template_name = 'notes_app/note_form.html'  # 👈 Ensure this matches
    success_url = reverse_lazy('notes-list')


class NoteDeleteView(DeleteView):
    model = Note
    template_name = 'note_confirm_delete.html'
    success_url = reverse_lazy('notes-list')

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after registration (optional)
            return redirect("login")  # Redirect to login page
    else:
        form = UserCreationForm()
    
    return render(request, "register.html", {"form": form})


