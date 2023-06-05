from django.forms import ModelForm

from .models import Posts, Comment


class PostForm(ModelForm):
    class Meta:
        model = Posts
        fields = ["title", "caption", "file"]


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["body"]
