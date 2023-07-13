from django.urls import path
from .views import list, ListLivres
urlpatterns = [
    path('list', list, name="livre"),
    path('livres', ListLivres.as_view(), name="livres")

]
