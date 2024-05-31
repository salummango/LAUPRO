# from django.contrib import admin
# from .models import Post
# from django import forms
# from ckeditor.widgets import CKEditorWidget

# # Register your models here.


# class PostAdminForm(forms.ModelForm):
#     body = forms.CharField(widget=CKEditorWidget())

#     class Meta:
#         model = Post
#         fields = '__all__'

# class PostAdmin(admin.ModelAdmin):
#     form = PostAdminForm

#     list_display=('title','slug','author','publish','status')
#     list_filter=('status','created','publish','author')
#     search_fields=('title','body')
#     prepopulated_fields={'slug':('title',)}
#     raw_id_fields=('author',)
#     date_hierarchy='publish'
#     ordering=('status','publish')
    
# admin.site.register(Post, PostAdmin)


from django.contrib import admin
from .models import Post
from django import forms
from tinymce.widgets import TinyMCE

class PostAdminForm(forms.ModelForm):
    body = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    class Meta:
        model = Post
        fields = '__all__'

class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm

    list_display=('title','slug','author','publish','status')
    list_filter=('status','created','publish','author')
    search_fields=('title','body')
    prepopulated_fields={'slug':('title',)}
    raw_id_fields=('author',)
    date_hierarchy='publish'
    ordering=('status','publish')

admin.site.register(Post, PostAdmin)

