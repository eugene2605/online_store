from django import forms
from catalog.models import Product, Version


class ProductForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Product
        fields = ('name', 'description', 'image', 'category', 'price')

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        for word in forbidden_words:
            if word in cleaned_data:
                raise forms.ValidationError('Наименование содержит запрещенные слова')
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        for word in forbidden_words:
            if word in cleaned_data:
                raise forms.ValidationError('Описание содержит запрещенные слова')
        return cleaned_data


class VersionForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Version
        fields = ('product', 'version_number', 'version_name', 'is_active')
