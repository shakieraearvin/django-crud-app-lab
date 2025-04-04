from django.urls import path
from . import views


urlpatterns = [

   path('', views.Home.as_view(), name='home'),
   path('about/', views.about, name='about'),
   path('recipes/', views.recipe_index, name='recipe-index'),
   path('recipes/<int:recipe_id>/', views.recipe_detail, name='recipe-detail'),
   path('recipes/create/', views.RecipeCreate.as_view(), name='recipe-create'),
   path('recipes/<int:pk>/update/', views.RecipeUpdate.as_view(), name='recipe-update'),
   path('recipes/<int:pk>/delete/', views.RecipeDelete.as_view(), name='recipe-delete'),
   path('recipes/<int:recipe_id>/add_meal/', views.add_meal, name='add-meal'),
   path('comments/create/', views.CommentCreate.as_view(), name='comment-create'),
   path('comments/<int:pk>/', views.CommentDetail.as_view(), name='comment-detail'),
   path('comments/', views.CommentList.as_view(), name='comment-index'),
   path('comments/<int:pk>/update/', views.CommentUpdate.as_view(), name='comment-update'),
   path('comments/<int:pk>/delete/', views.CommentDelete.as_view(), name='comment-delete'),
   path('accounts/signup/', views.signup, name='signup'),





]
