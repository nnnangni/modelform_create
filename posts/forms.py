from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta: # 만들고 있는 PostForm이라는 클래스에 내부 설정들을 저장하는 클래스
        model = Post
        fields = '__all__'