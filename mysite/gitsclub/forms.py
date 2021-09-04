from django import forms


class UserIdForm(forms.Form):
    UserId = forms.CharField(max_length=100,widget=forms.TextInput({"placeholder" : "GitHub Username"}))