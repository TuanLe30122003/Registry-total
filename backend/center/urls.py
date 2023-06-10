from django.urls import path
from . import views

urlpatterns = [
    path('center/', views.center1, name='center'),
    path('centers/', views.center_list, name='center-list'),
    path('inspections/', views.inspection_list, name='inspection_list'),
    path('owners/', views.owner_list, name='owner_list'),
    path('registrations/', views.registration_list, name='registration_list'),

    path('month_center/', views.month_center, name='month_center'),
    path('quarter_center/', views.quarter_center, name='quarter_center'),
    path('year_center/', views.year_center, name='year_center'),

    path('month_Area/', views.month_Area, name='month_Area'),
    path('quarter_Area/', views.quarter_Area, name='quarter_Area'),
    path('year_Area/', views.year_Area, name='year_Area'),

    path('month_Country/', views.month_Country, name='month_Country'),
    path('quarter_Country/', views.quarter_Country, name='quarter_Country'),
    path('year_Country/', views.year_Country, name='year_Country'),

    path('expired_month_center/', views.expired_month_center,
         name='expired_month_center'),
    path('expired_month_Area/', views.expired_month_Area,
         name='expired_month_Area'),
    path('expired_month_Country/', views.expired_month_Country,
         name='expired_month_Country'),

    path('forecast_expired_month_center/', views.forecast_expired_month_center,
         name='forecast_expired_month_center'),
    path('forecast_expired_month_Area/', views.forecast_expired_month_Area,
         name='forecast_expired_month_Area'),
    path('forecast_expired_month_Country/', views.forecast_expired_month_Country,
         name='forecast_expired_month_Country'),
]
