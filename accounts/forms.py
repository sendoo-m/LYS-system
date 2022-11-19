from django import forms

class UserLoginForm(forms.Form):
    username        = forms.CharField(widget=forms.TextInput(
        attrs       = {"class": "form-control", "placeholder": "اسم المستخدم"}))
    password        = forms.CharField(widget=forms.PasswordInput(
        attrs       = {"class": "form-control", "placeholder": "كلمة المرور"}))

