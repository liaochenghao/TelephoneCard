from django.conf.urls import url, include

urlpatterns = [
    url(r'^api/v1/', include('user_info.urls')),
]
