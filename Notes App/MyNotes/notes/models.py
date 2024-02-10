from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=300)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) # chestia asta cu true  inseamna ca se pune automat data si ora cand se creeaza notita
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')
    # on_delete=models.CASCADE = daca userul asociat cu o nota este sters, se sterge si notita asociata
    # related_name='notes' = permite accesarea notitelor create de user, de catre userul respectiv

# deci charfield este un camp care stocheaza character data, siruri de text scurte: titluri, text scurt, este conceput special pentru un text micut cu lungime specificata