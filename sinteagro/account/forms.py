from django import forms

from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name","last_name","email","sexo","estado","cidade","nascimento","password"]
        labels = {"first_name": "Nome", "last_name": "Sobrenome", "email": "E-mail", "sexo": "Sexo", "estado": "Estado", "cidade": "Cidade", "nascimento": "Data de Nacimento", "password": "Senha"}

    def check_password(self):
        if len(str(self.fields["password"])) < 6 or len(str(self.fields["password"])) > 8:
            return False
        else:
            return True