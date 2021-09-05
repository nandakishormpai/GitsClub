from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from .models import User
from .forms import UserRegisterForm
from .functions import getUserInfo
# Create your views here.


def index(request):
    return render(request, 'index.html')


'''
def newmember(request):
    if request.method == 'POST':
        print("\n\n\nhere\n\n\n\n")
        form = UserIdForm(request.POST)
        if form.is_valid():
            form.save()
            userid = form.cleaned_data.get('UserId')
            # userData = newDataFetch(userId)
            User.objects.create(userId=userid, profilePic="https://avatars.githubusercontent.com/u/53964426?v=4",
                                name="HariU", bio="CETIAN", starCount=2, repoCount=26, followerCount=4)
            # user = User(userId=userId,profilePic="https://avatars.githubusercontent.com/u/53964426?v=4", name="HariU", bio="CETIAN", starCount=2, repoCount=26, followerCount=4)
            # user.save()
            return redirect('groups')
    else:
        form = UserIdForm()
    context = {'form': form}
    return render(request, 'newmember.html', context)
'''


def groups(request):
    if request.method == 'POST':
        print("\n Was here \n")
        # update(db)
    users = User.objects.all()
    return render(request, 'groups.html', {'users': users})


def group(request, id):

    return HttpResponse("Each group Here  " + str(id))


def newmember(request):
    form = UserRegisterForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        userId = form.cleaned_data['userId']
        print("\n\n"+str(userId)+"\n\n")
        # userinfo = User(userId=userId, profilePic="https://avatars.githubusercontent.com/u/53964426?v=4",
        #             name="HariU", bio="CETIAN", starCount=2, repoCount=26, followerCount=4)
        # User.objects.create(userId=userId, profilePic="https://avatars.githubusercontent.com/u/53964426?v=4",
        #                     name="HariU", bio="CETIAN", starCount=2, repoCount=26, followerCount=4)
        userData = getUserInfo([userId])
        User.objects.create(
            userId=userId,
            profilePic=userData[userId]["profileURL"],
            name=userData[userId]["name"],
            bio=userData[userId]["bio"],
            starCount=userData[userId]["starCount"],
            repoCount=userData[userId]["repoCount"],
            followerCount=userData[userId]["followerCount"],
        )
        messages.success(request, f'Success for {userId}!')
        return redirect('groups')
    else:
        form = UserRegisterForm()
    return render(request, 'newmember.html', {'form': form})
    # def about(request):
    #     return render(request,'index.html/#about')


def refresh(request):
    print("\n Was here \n")
    # update(db)
    return redirect('groups')
