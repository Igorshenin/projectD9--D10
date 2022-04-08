from django.urls import path
from .views import *  # импортируем наше представление

urlpatterns = [
    path('', PostListView.as_view(), name='news'),
    path('<int:pk>', NewDetail.as_view(), name='new_detail'),
    path('create/', PostCreateView.as_view(), name='news_create'),
    path('create/<int:pk>', PostUpdateView.as_view(), name='new_update'),
    path('delete/<int:pk>', PostDeleteView.as_view(), name='new_delete'),
    path('upgrade/', upgrade_me, name='upgrade'),
    path('categories/', CategoriesListView.as_view(), name='categories_list'),
    path('categories/<int:pk>', PostsCategoryListView.as_view(), name='posts_category'),
    path('subscribe/', subscribe, name='subscribe'),

    # pk — это первичный ключ новости, который будет выводиться у нас в шаблон
    # т. к. сам по себе это класс, то нам надо представить этот класс в виде view.
    # Для этого вызываем метод as_view
]