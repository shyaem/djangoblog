from django import forms
from . models import Detail


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Detail
        fields = ['displayphoto', 'displayname',
                  'mobile', 'dob', 'email', 'bio']
