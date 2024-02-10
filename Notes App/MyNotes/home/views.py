from django.views.generic import TemplateView, CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

# Create your views here.
class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'home/signup.html'
    success_url = reverse_lazy('login')
class LoginInterfaceView(LoginView):
    template_name = 'home/login.html'
class LogoutInterfaceView(LogoutView):
    template_name = 'home/logout.html'

# am pus asta pentru ca tot aparea eroarea "Method Not Allowed (GET): /logout/; Method Not Allowed: /logout/
# deci metoda de dispatch asigură că cererile primite sunt direcționate corect către handlerul de metodă corespunzător
# dacă cererea = solicitare GET, se apelează metoda get a vizualizării (self.get(request, *args, **kwargs))
# non-GET = POST, PUT, DELETE etc., cererile non-GET sunt gestionate de o metoda adecvată bazată pe HTTP

    def dispatch(self, request, *args, **kwargs):
        if request.method == 'GET':
            return self.get(request, *args, **kwargs)
        else:
            return super().dispatch(request, *args, **kwargs)

class HomeView(TemplateView):
    template_name = 'home/welcome.html'
