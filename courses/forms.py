from django import forms
from django.forms import SelectMultiple, TextInput, Textarea

from courses.models import Course

# class CourseCreateForm(forms.Form):
#     title = forms.CharField(
#         label="course title", 
#         required=True,
#         error_messages={
#             "required": "you must enter the course title"}, 
#         widget=forms.TextInput(attrs={ "class":"form-control" }))
    
#     description = forms.CharField(widget=forms.Textarea(attrs={ "class":"form-control" }))
#     imageUrl = forms.CharField(widget=forms.TextInput(attrs={ "class":"form-control" }))
#     slug = forms.SlugField(widget=forms.TextInput(attrs={ "class":"form-control" }))

class CourseCreateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('title', 'description', 'image', 'slug')
        labels = {
            'title': "course title",
            'description': "description"
        }
        widgets = {
            "title": TextInput(attrs={ "class": "form-control" }),
            "description": Textarea(attrs={ "class": "form-control" }),
            "slug": TextInput(attrs={ "class": "form-control" }),
        }
        error_messages = {
            "title": {
                "required": "you must enter the course title",
                "max_length": "you must enter a maximum of fifty characters"
            },
            "description": {
                "required": "course description required"
            }
        }
        
class CourseEditForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('title', 'description', 'image', 'slug', 'categories', 'isActive')
        labels = {
            'title': "course title",
            'description': "description"
        }
        widgets = {
            "title": TextInput(attrs={ "class": "form-control" }),
            "description": Textarea(attrs={ "class": "form-control" }),
            "slug": TextInput(attrs={ "class": "form-control" }),
            "categories": SelectMultiple(attrs={ "class": "form-control" })
        }
        error_messages = {
            "title": {
                "required": "you must enter the course title",
                "max_length": "you must enter a maximum of fifty characters"
            },
            "description": {
                "required": "course description required"
            }
        }
        
class UploadForm(forms.Form):
    image = forms.ImageField()