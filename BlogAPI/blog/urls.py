from django.urls import path
from . import views
# from django.conf import settings
# from django.conf.urls.static import static
# +static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns = [
    # path for user
    path('usercreate', views.UserCreateAPI.as_view()),
    path('useralldata', views.UserDataAPI.as_view()),
    path('useronedata/<int:pk>', views.UserOneDataAPI.as_view()),
    path('userupdate/<int:pk>',views.UserUpdateAPI.as_view()),
    path('userupt/<int:pk>', views.UserUpdatePartialAPI.as_view()),
    path('userdelete/<int:pk>', views.UserDeleteAPI.as_view()),

    # path for posts
    path('postcreate', views.PostCreateAPI.as_view()),
    path('postalldata', views.PostDataAPI.as_view()),
    path('postonedata/<int:pk>', views.PostOneDataAPI.as_view()),
    path('postupdate/<int:pk>',views.PostUpdateAPI.as_view()),
    path('postupt/<int:pk>', views.PostUpdatePartialAPI.as_view()),
    path('postdelete/<int:pk>', views.PostDeleteAPI.as_view()),

    # path for like
    path('likecreate', views.LikeCreateAPI.as_view()),
    path('likealldata', views.LikeDataAPI.as_view()),
    path('likeonedata/<int:pk>', views.LikeOneDataAPI.as_view()),
    path('likeupdate/<int:pk>',views.LikeUpdateAPI.as_view()),
    path('likeupt/<int:pk>', views.LikeUpdatePartialAPI.as_view()),
    path('likedelete/<int:pk>', views.LikeDeleteAPI.as_view()),
]