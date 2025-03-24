from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class ScrapeForm(forms.Form):
    url = forms.URLField(label='Playlist URL', max_length=200)

    def __init__(self, *args, **kwargs):
        super(ScrapeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Scrape'))