# from django import forms
# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Submit
from django.forms import forms

# from .models import Post, Comment
#
#
# class PostForm(forms.ModelForm):
#     image = forms.ImageField(label='Завантажити картинку')
#
#     class Meta:
#         model = Post
#         fields = ['title', 'content', 'image']
#
#
#     def __init__(self, *args, **kwargs):
#         super(PostForm, self).__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper_method = 'post'
#         self.helper.add_input(Submit('submit', 'Зберегти'))


# class CommentForm(forms.ModelForm):
#
#     class Meta:
#         model = Comment
#         fields = ('username', 'body',)
