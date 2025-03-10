from django import forms

class CourseCreateForm(forms.Form):
    title = forms.CharField()
    description = forms.ChoiceField(widget=forms.Textarea)
    imageUrl = forms.CharField()
    slug = forms.SlugField()