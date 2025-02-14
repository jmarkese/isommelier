from django.urls import path
from django.urls import re_path
from django.conf.urls import url, include
from winereviews.views import ReviewList, ReviewUpdate, ReviewDelete
from winereviews.views import WineList, WineCreate, WineUpdate, WineDelete
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('consultancy/', views.consultancy, name='consultancy'),
    path('worldmap-template/', views.winebycountry, name='worldmap-template'),
    path('wine_variety_stats/', views.wine_variety_stats, name='wine_variety_stats'),
    path('wine_country_report/<countryName>/', views.wine_country_report, name='wine_country_report'),
    path('variety_options/', views.variety_options, name='variety_options'),
    path('variety_reviews/<int:variety_id>', views.variety_reviews, name='variety_reviews'),
    path('wine_review_search/', views.wine_review_search, name='wine_review_search'),
    path('wine_data_viz/', views.wine_data_viz, name='wine_data_viz'),
    path('word_count_stats/<int:number>', views.word_count_stats, name='word_count_stats'),
    path('word_count_stats_expensive/<int:number>', views.word_count_stats_expensive, name='word_count_stats_expensive'),
    path('word_count_stats_rating_hi/<int:number>', views.word_count_stats_rating_hi, name='word_count_stats_rating_hi'),
    path('word_count_stats_rating_lo/<int:number>', views.word_count_stats_rating_lo, name='word_count_stats_rating_lo'),
    
    # Reviews CRUD
    path('review_create/', views.review_create, name='review_create'),
    path('review_delete/<int:review_id>', views.review_delete, name='review_delete'),
    path('review_like/<int:review_id>', views.review_like, name='review_like'),

    path('reviews/', ReviewList.as_view(), name ='reviews'),
    path('review/<int:pk>/', views.review_update, name='review_update'),
    path('review/<int:pk>/delete/', views.review_delete_actual, name='review_delete_actual'),
    path('review/<int:pk>/detail', views.review_detail, name='review_detail'),

    # Wines CRUD
    path('wines/', WineList.as_view(), name='wine_list'),
    path('wine/add/', WineCreate.as_view(), name='wine_add'),
    path('wine/<int:pk>/', WineUpdate.as_view(), name='wine_update'),
    path('wine/<int:pk>/delete/', WineDelete.as_view(), name='wine_delete'),
    path('wine/<int:pk>/detail', views.wine_detail, name='wine_detail'),
    path('wine/<int:pk>/review/', views.wine_review_create, name='wine_review_create'),

    path('wine_type_ahead/', views.wine_type_ahead, name='wine_type_ahead'),

    # path('type_ahead/<str:model>/<str:search>/', views.type_ahead, name='type_ahead'),
    # path('type_ahead/<str:model>/<str:search>/<str:show>/', views.type_ahead, name='type_ahead'),
]
