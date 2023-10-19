from django.urls import path,include
from . import views
from myapp.views import RegisterView
from .views import ImageList, ImageDetail, upload_image
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r'images', ImageViewSet)


urlpatterns = [
    path("", views.user_auth),
    path("user_list/", views.user_list),
    path("register/", RegisterView.as_view(), name="auth_register"),
    path('images/', ImageList.as_view(), name='image-list'),
    path('images/<int:pk>/', ImageDetail.as_view(), name='image-detail'),
    path('image/upload', upload_image, name="upload-image")
    # path('', include(router.urls)),
    

]
