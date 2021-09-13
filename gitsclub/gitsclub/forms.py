from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError
from django import forms
from django.forms import widgets
from .models import User, Member


# User Register Form for Custom User
class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField()
    githubuserId = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Github Username', 'class': 'input100'}),)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = Member
        fields = ['email', 'githubuserId']

    def clean_email(self):
        '''
        Verify email is available.
        '''
        email = self.cleaned_data.get('email')
        qs = Member.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("email is taken")
        return email

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class GroupJoinForm(forms.Form):
    try:
        userId = forms.CharField(widget=forms.TextInput(
            attrs={'placeholder': 'Github Username', 'class': 'input100'}),)
        groups = User.objects.values_list('groupName').distinct()
        groups_list = list()
        for i, group in enumerate(groups):
            groups_list.append(tuple([group[0], group[0]]))
        group_list = tuple(groups_list)
        groupName = forms.ChoiceField(choices=group_list)

        class Meta:
            model = User
            fields = ['userId', 'groupName']
    except:
        userId = forms.CharField(widget=forms.TextInput(
            attrs={'placeholder': 'Github Username', 'class': 'input100'}),)
        groupName = forms.CharField(widget=forms.TextInput(
            attrs={'placeholder': 'Create Group', 'class': 'input100'}),)

        class Meta:
            model = User
            fields = ['userId', 'groupName']


class GroupCreateForm(forms.Form):
    userId = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Github Username', 'class': 'input100'}),)
    groupName = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Create Group', 'class': 'input100'}),)

    class Meta:
        model = User
        fields = ['userId', 'groupName']
