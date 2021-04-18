from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('languages', views.LanguageView, basename='languageModel'),

urlpatterns = [
    path('', views.home),
    path('chat/', views.chatView),
    path('loginView/', views.loginView),
#    path('getMessages/',views.getMessageView),
#    path('chat/sendMessages/',views.sendMessageView),
    path('', include(router.urls))
]
