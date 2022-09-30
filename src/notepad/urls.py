from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path


from notes.views import delete_item, finish_item, note_list_view, recover_item

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', note_list_view, name='note-list'),
    path('finish-item/<id>/', finish_item, name='finish-item'),
    path('delete-item/<id>/', delete_item, name='delete-item'),
    path('recover-item/<id>/', recover_item, name='recover-item'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, 
                         document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, 
                         document_root = settings.MEDIA_ROOT)

