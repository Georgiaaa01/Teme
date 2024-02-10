from .models import Note
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from . forms import NotesForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect

# Create your views here.

class NotesDeleteView(LoginRequiredMixin, DeleteView): # responsabil pt stergerea notitelor
    model = Note
    success_url = '/category/notes/'
    template_name = 'notes/note_delete.html'
    login_url = '/login'

# prin asta se da override la metoda de get_queryset pt a se returna doar notitele care aparțin de userul "curent"
    def get_queryset(self):
        return self.request.user.notes.all()

class NotesUpdateView(LoginRequiredMixin, UpdateView): # responsabil pt actualizare de notite
    model = Note
    success_url = '/category/notes/'
    form_class = NotesForm
    login_url = '/login'

    def get_queryset(self):
        return self.request.user.notes.all()

class NotesCreateView(LoginRequiredMixin, CreateView): # responsabil pt crearea de noi notite
    model = Note
    success_url = '/category/notes/'
    form_class = NotesForm
    login_url = '/login'

    def form_valid(self, form):
        self.object = form.save(commit=False) # salveaza datele din formular in modelul Note dar nu le salveaza in baza de date
        self.object.user = self.request.user # utilizatorului curent (cel care a facut notita) i se atribuie notita
        self.object.save() # salveaza notita modificata in baza de date, cu toate ca initial aveam commit=False, save() face sa se salveze modificarile in baza de date
        return HttpResponseRedirect(self.get_success_url()) # ne trimite inapoi la lista

class NotesListView(LoginRequiredMixin, ListView):
    model = Note
    context_object_name = "notes"
    login_url = '/login'

    def get_queryset(self):
        return self.request.user.notes.all()

# prin LoginRequiredMixin ne asiguram ca numai userii logati pot sa acceseze notitele





