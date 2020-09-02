from django.contrib import admin
from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
	list_display=('name','company','created_on',)
	list_filter=("year","company")
	search_fields = ['name','company','branch','year','type_of_place',]
	#prepopulated_fields = {'slug': ('title',)}



admin.site.register(Post,PostAdmin)