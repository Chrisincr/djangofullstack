from django.urls import path
from . import views

urlpatterns = [
    path('', views.shows),
    path('shows', views.shows),
    path('shows/new', views.shows_new),
    path('shows/create', views.shows_create),
    path('shows/<int:id>', views.shows_show),
    path('shows/<int:id>/edit', views.shows_edit),
    path('shows/<int:id>/update', views.shows_update),
    path('shows/<int:id>/destroy', views.shows_destroy),
]