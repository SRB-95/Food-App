from . import views
from django.urls import path

app_name = 'food'
urlpatterns = [
    #/food/
    path('', views.IndexClassView.as_view(),name="index"),
    #/food/id(id of food might be 1/2/3...))
    path('<int:pk>/', views.FoodDetail.as_view(), name='detail'),
    # add items
    path('add',views.CreateItem.as_view(),name="create_item"),
    # edit items
    path('update/<int:id>/',views.update_item,name='update_item'),
    # delete items
    path('delete/<int:id>/',views.delete_item,name='delete_item'),
    # Search items
    path('search/',views.searchFunctionality,name='search'),

]