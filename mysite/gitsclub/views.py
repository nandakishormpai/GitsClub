from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import User
from .forms import UserIdForm
# Create your views here.


def index(request):
    return render(request, 'index.html')


def newmember(request):
    if request.method == 'POST':
        print("\n\n\nhere\n\n\n\n")
        form = UserIdForm(request.POST)
        if form.is_valid():
            form.save()
            userid=form.cleaned_data.get('UserId')
            # userData = newDataFetch(userId)
            User.objects.create(userId=userid,profilePic="https://avatars.githubusercontent.com/u/53964426?v=4", name="HariU", bio="CETIAN", starCount=2, repoCount=26, followerCount=4 )
            # user = User(userId=userId,profilePic="https://avatars.githubusercontent.com/u/53964426?v=4", name="HariU", bio="CETIAN", starCount=2, repoCount=26, followerCount=4)
            # user.save()
            return redirect('groups')
    else:
        form = UserIdForm()
    context = {'form':form } 
    return render(request, 'newmember.html', context)




def groups(request):
    users = User.objects.all()
    return render(request, 'groups.html', {'users': users})


def group(request, id):
    return HttpResponse("Each group Here  " + str(id))

# def about(request):
#     return render(request,'index.html/#about')
