from django.urls import path
from demo_app import views
from django.views.decorators.cache import cache_page


urlpatterns = [
    path('', cache_page(36000)(views.home), name='home'),
    path('detail/', cache_page(36000)(views.detail), name='detail'),
]


