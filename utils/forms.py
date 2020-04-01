from django import forms
from ckeditor.widgets import CKEditorWidget


class WriteForm(forms.Form):
    blog_text = forms.CharField(widget=CKEditorWidget(config_name='article_config'))
