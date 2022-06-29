from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('categoryproducts/<category>',
         views.GetPruducts.as_view(), name='categoryproducts'),
    path('topratedroducts/',
         views.GetTopRatedPruducts.as_view(), name='categoryproducts'),
    path('categories/', views.GetCategories.as_view(), name='categories'),
    path('mostsaled/', views.MostSaledPruducts.as_view(), name='mostsaled'),
    path('newrate/<id>', views.NewRate.as_view(), name='newRate'),
    path('updaterate/<pk>', views.UpdateRate.as_view(), name='updateRate'),
    # path('resetpasswordcode/', views.ResetPasswordCode.as_view(), name='resetcode'),
]
