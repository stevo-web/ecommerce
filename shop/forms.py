from django.forms import ModelForm
from main.models import Product


class AddProductForm(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        exclude = ('shop',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control validate'})
        self.fields['price'].widget.attrs.update({'class': 'form-control validate'})
        self.fields['discount'].widget.attrs.update({'class': 'form-control validate'})
        self.fields['image'].widget.attrs.update({'class': 'form-control validate'})
        self.fields['description'].widget.attrs.update({'class': 'form-control validate'})
        self.fields['category'].widget.attrs.update({'class': 'form-control w-100 validate'})
