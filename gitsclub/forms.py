from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import widgets


class UserRegisterForm(forms.Form):
    userId = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Github Username', 'class': 'input100'}),)

    class Meta:
        model = User
        fields = ['userId']
    '''
    def clean(self, *args, **kwargs):
        userId = self.cleaned_data['username']
        return super(UserRegisterForm, self).clean(*args, **kwargs)
    
    def save(self, *args, **kwargs):
        user = User(userId=self.cleaned_data['userId'], profilePic="https://avatars.githubusercontent.com/u/53964426?v=4",
                    name="HariU", bio="CETIAN", starCount=2, repoCount=26, followerCount=4)
        User.objects.create(user=user)
    '''


'''
class UserIdForm(forms.Form):
    UserId = forms.CharField(max_length=100,widget=forms.TextInput({"placeholder" : "GitHub Username"}))
'''
