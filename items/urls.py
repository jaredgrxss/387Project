from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'items'

urlpatterns = [
    path('',views.ListItems.as_view(),name='all-items'),
    path('details/<int:pk>',views.DetailItem.as_view(),name='item-detail'),
    path('createitem/',views.CreateItem.as_view(),name='create-item'),
    path('delete/<int:pk>',views.DeleteItem.as_view(),name='delete-item'),
    path('update/<int:pk>',views.UpdateItem.as_view(),name='update-item'),
    path('createbid/',views.CreateBid.as_view(),name='create-bid'),
    path('userprofile/',views.user_profile,name='list_user'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

