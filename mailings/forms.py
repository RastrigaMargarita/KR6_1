from django import forms
from mailings.models import Settings

class MailingForm(forms.ModelForm):
    class Meta:
        model = Settings
        fields = ['start_date', 'period', 'status', 'message', 'client']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

