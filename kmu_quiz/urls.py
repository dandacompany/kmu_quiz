from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "KMU Quiz 관리자"
admin.site.site_title = "KMU Quiz 관리자"
admin.site.index_title = "KMU Quiz 관리"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('quiz.urls')),  # 퀴즈 앱의 URL을 루트 URL에 연결
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)