from django import forms
from django.forms import ModelForm
from .models import Listing
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout , Field



class ProductForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ['title', 'photo_main', 'photo_1', 'photo_2', 'photo_3', 'photo_4', 'photo_5', 'photo_6', 'description', 'quantity', 
                'category', 'price', 'is_published', 'address', 'city', 'zipcode', 'delivery']
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('photo_main', template='baseinput.html')
        )
        self.helper.form_show_labels = False
        self.fields['photo_main'].help_text = None
        self.fields['photo_main'].widget.attrs.update({'placeholder': 'Title', 'class':'form-control-file my-file-input'})
        self.fields['photo_1'].widget.attrs.update({'placeholder': 'Title', 'class':'form-control-file my-file-input'})
        self.fields['photo_2'].widget.attrs.update({'placeholder': 'Title', 'class':'form-control-file my-file-input'})
        self.fields['photo_3'].widget.attrs.update({'placeholder': 'Title', 'class':'form-control-file my-file-input'})
        self.fields['photo_4'].widget.attrs.update({'placeholder': 'Title', 'class':'form-control-file my-file-input'})
        self.fields['photo_5'].widget.attrs.update({'placeholder': 'Title', 'class':'form-control-file my-file-input'})
        self.fields['photo_6'].widget.attrs.update({'placeholder': 'Title', 'class':'form-control-file my-file-input'})
    