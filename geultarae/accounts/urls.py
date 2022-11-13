from django.urls import include, path

app_name = 'accounts'
urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
]