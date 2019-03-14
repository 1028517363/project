from django import forms
from comment.models import Comments

class UserMovieCommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        filter('user', 'comment')

