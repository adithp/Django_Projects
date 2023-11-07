from django import forms
from posts.models import Post


class PostForm(forms.ModelForm):
    categories = forms.CharField(widget=forms.TextInput(attrs={'class':"input"}),label="Tags (Comma seperated) ")
    class Meta:
        model = Post
        exclude = ('author','published_date','is_deleted','categories')
        
        widgets = {
            "time_to_read" : forms.TextInput(attrs={'class':"input"}),
            "title" : forms.TextInput(attrs={'class':"input"}),
            "short_description" : forms.Textarea(attrs={'class':"input"}), 
        }
        
        error_messages = {
            'title':{
                'required':"Title field is required",
            },
            'description':{
                'required':"description field is required",
            },
            'short_description':{
                'required':"short_description field is required",
            },
            'time_to_read':{
                'required':"time_to_read field is required",
            }
        }


