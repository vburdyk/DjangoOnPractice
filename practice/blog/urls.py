from django.urls import path

from .views import *

urlpatterns = [
    path('', index),
    path('auth', auth_page, name='auth.page'),
    path('auth/login', auth_page_login, name='auth.login'),

    path('signup', signup, name='signup'),
    path('logout', logout, name='logout'),
    path('upload', upload, name='upload'),
    path('upload/submit', upload_submit, name='upload.submit'),
    path('delete/<post_id>', delete_post, name='delete'),
    path('like-post', like_post, name='like-post'),
    path('make-comment/<str:post_id>', make_comment_page, name='make-comment'),
    path('make-comment/send/<str:post_id>', make_comment_send, name='make-comment.send')

]
