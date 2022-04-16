from django.contrib import admin
from django.urls import include, path
from main.views import index
from django.conf import settings
from django.conf.urls.static import static
from review.views import  blog, posting,new_post,remove_post

urlpatterns = [
    path('board/', include('board.urls')),
    path('', index ,name='index' ),
    #Admin 사이트 url
    path('admin/', admin.site.urls),
    #로그인,로그아웃, url
    # path('auth/', include("users.urls")),
    
    #인기장소
    path('place_list/', include("hot_place.urls")),
    #테마선택
    path('theme_list/', include("theme.urls")),
     #공지사항
    path('notice_page/',include("notice.urls")),

    #후기페이지
    path('blog/', blog, name='blog'),
    # URL:80/blog/숫자로 접속하면 게시글-세부페이지(posting)
    path('blog/<int:pk>/',posting, name="posting"),
    path('blog/new_post/', new_post),
    path('blog/<int:pk>/remove/', remove_post),
    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)