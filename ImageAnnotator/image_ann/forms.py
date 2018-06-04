from django import forms
from image_ann.models import Hit
class FormAMT(forms.ModelForm):
    class Meta:
        model = Hit
        fields = ('body',)

        widgets = {
            'body': forms.Textarea(attrs={'width':"100%", 'cols' : "80", 'rows': "20"})
            }

    # the forms will contain the assignment ID that will be sent back to Amazon
    assignmentId = forms.CharField(widget = forms.HiddenInput)
