from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("main.urls")),
    path('news/', include('news.urls')), #все URL-адреса, начинающиеся с "news/", будут передаваться в обработку в файл
                                         #"news.urls", где будут определены соответствующие представления (views) для
                                         #этих URL-адресов
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)