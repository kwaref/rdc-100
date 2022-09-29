from django.urls import path
from .views import ClipList, ClipDetail

# urlpatterns = [
#     path('clips/', views.ClipView.as_view(), name='clips_list'),
# ]
urlpatterns = [
    path('<int:pk>/', ClipDetail.as_view(), name='detailcreate'),
    path('', ClipList.as_view(), name='listcreate'),
]
