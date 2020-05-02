# -*- coding: utf-8 -*-
from django.urls import path

from . import views

urlpatterns = [
    path('index.html', views.index, name='index'),
    path('charts-chartjs.html', views.index1, name='index1'),
    path('components-accordions.html', views.index2, name='index2'),
    path('components-calendar.html', views.index3, name='index3'),
    path('components-carousel.html', views.index4, name='index4'),
    #path('/components-carousel.html', views.index, name='index5'),
    path('components-modals.html', views.index6, name='index6'),
    path('components-notifications.html', views.index7, name='index7'),
    path('components-pagination.html', views.index8, name='index8'),
    path('components-progress-bar.html', views.index9, name='index9'),
    path('components-scrollable-elements.html', views.index10, name='index10'),
    path('components-tabs.html', views.index11, name='index11'),
    path('components-tooltips-popovers.html', views.index12, name='index12'),
    path('dashboard-boxes.html', views.index13, name='index13'),
    path('elements-badges-labels.html', views.index14, name='index14'),
    path('elements-buttons-standard.html', views.index15, name='index15'),
    path('elements-cards.html', views.index16, name='index16'),
    path('elements-dropdowns.html', views.index17, name='index17'),
    path('elements-icons.html', views.index18, name='index18'),
    path('elements-list-group.html', views.index19, name='index19'),
    path('elements-navigation.html', views.index20, name='index20'),
    path('elements-utilities.html', views.index21, name='index21'),
    path('forms-controls.html', views.index22, name='index22'),
    path('forms-layouts.html', views.index23, name='index23'),
    path('forms-validation.html', views.index24, name='index24'),
    path('tables-regular.html', views.index25, name='index25'),
    path('hi', views.table, name='table'),
    #path('', views.index, name='index25'),
   #path('', views.index, name='index23'),
]
