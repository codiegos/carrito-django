from django import forms
from django.forms import widgets
from .models import Usuario,TipoUsuario,Disco,TipoDisco

class UsuarioForm(forms.ModelForm):
    tipoUsuario = forms.ModelChoiceField(queryset=TipoUsuario.objects.all(),label="Tipo Usuario")

    class Meta:
        model = Usuario
        fields = '__all__'
        widgets = {
            'nombre': widgets.TextInput(attrs={'class':'form-control','min_length':3}),
            'apellido': widgets.TextInput(attrs={'class':'form-control','min_length':3}),
            'fecha_nacimiento': widgets.DateInput(attrs={'type': 'Date','class':'form-control'}),
        }
    
    tipoUsuario.widget.attrs['class'] = 'form-select'

class TipoUsuarioForm(forms.ModelForm):
    class Meta:
        model = TipoUsuario
        fields = '__all__'
        widgets = {
            'nombre': widgets.TextInput(attrs={'class':'form-control','min_length':3}),
        }

class DiscoForm(forms.ModelForm):
    tipoDisco = forms.ModelChoiceField(queryset=TipoDisco.objects.all(),label="Tipo Disco")

    class Meta:
        model = Disco
        fields = '__all__'
        widgets = {
            'codigo': widgets.TextInput(attrs={'class':'form-control','min_length':3}),
            'nombre': widgets.TextInput(attrs={'class':'form-control','min_length':3}),
            'descripcion': widgets.TextInput(attrs={'class':'form-control','min_length':3}),
            'valor': widgets.NumberInput(attrs={'class':'form-control'}),
            'url_imagen': widgets.TextInput(attrs={'class':'form-control','min_length':7}),
            'stock': widgets.NumberInput(attrs={'class':'form-control'}),
        }
    
    tipoDisco.widget.attrs['class'] = 'form-select'

class TipoDiscoForm(forms.ModelForm):
    class Meta:
        model = TipoDisco
        fields = '__all__'
        widgets = {
            'nombre': widgets.TextInput(attrs={'class':'form-control','min_length':3}),
        }