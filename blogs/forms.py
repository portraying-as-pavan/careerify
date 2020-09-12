from django import forms




from .models import Post

class PostForm(forms.ModelForm):




	class Meta:
		model=Post
		fields=('name','photo','company','year','type_of_place','branch','title','content')
