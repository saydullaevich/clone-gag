from django.urls import path
from .views import *


app_name = 'main'

urlpatterns = [
    path('', MainIndex, name="index"),
    path('cat/<int:id>/', MainIndex, name="cat"),
    path('upload/', UploadPost.as_view(), name="upload"),
    path('post/<str:action>/<int:post_id>/', PostLike.as_view(), name="like"),
    path('comments/<int:post_id>/', PostCommentView.as_view(), name="comment")
]
