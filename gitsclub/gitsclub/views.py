from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.db.models import Sum
from .models import User
from .forms import GroupJoinForm, GroupCreateForm, UserRegisterForm
from .functions import getUserInfo
# Create your views here.


def index(request):
    group_count = len(User.objects.values_list('groupName').distinct())
    repo_count = User.objects.values('userId').distinct().annotate(
        total=Sum('repoCount')).aggregate(Sum('repoCount'))
    star_count = User.objects.values('userId').distinct().annotate(
        total=Sum('starCount')).aggregate(Sum('starCount'))
    user_count = len(User.objects.values_list('userId').distinct())
    return render(request, 'index.html', {'group_count': group_count, 'repo_count': repo_count['repoCount__sum'], 'star_count': star_count['starCount__sum'], 'user_count': user_count})


def groups(request):
    # Script below to refresh
    if request.method == 'POST':
        users = User.objects.values_list('userId').distinct()
        for user in users:
            userData = getUserInfo([user[0]])
            cur_users = User.objects.filter(userId=user[0])
            for cur_user in cur_users:
                cur_user.profilePic = userData[user[0]]["profileURL"]
                cur_user.name = userData[user[0]]["name"]
                cur_user.bio = userData[user[0]]["bio"]
                cur_user.starCount = userData[user[0]]["starCount"]
                cur_user.repoCount = userData[user[0]]["repoCount"]
                cur_user.followerCount = userData[user[0]]["followerCount"]
                cur_user.save()
    groups = User.objects.values_list('groupName').distinct()
    group_dict = dict()
    for group in groups:
        users = User.objects.filter(groupName=group[0])
        group_dict[group[0]] = users
    print(group_dict, "here")
    return render(request, 'groups.html', {'group_dict': group_dict})


def group(request, id):

    return HttpResponse("Each group Here  " + str(id))


def newmember(request):
    form = GroupJoinForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        userId = form.cleaned_data['userId']
        groupName = form.cleaned_data['groupName']
        if User.objects.filter(namegroupid=(userId+"_"+groupName)).exists():
            messages.success(request, f'{userId} Already Exists!')
            return redirect('newmember')
        # hard coded input to test
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
            groupName=groupName,
            namegroupid=userId + "_" + groupName
        )
        messages.success(request, f'Welcome {userId}!')
        return redirect('groups')
    else:
        form = GroupJoinForm()
        group_count = len(User.objects.values_list('groupName').distinct())
        repo_count = User.objects.values('userId').distinct().annotate(
            total=Sum('repoCount')).aggregate(Sum('repoCount'))
        star_count = User.objects.values('userId').distinct().annotate(
            total=Sum('starCount')).aggregate(Sum('starCount'))
        user_count = len(User.objects.values_list('userId').distinct())
    return render(request, 'newmember.html', {'form': form, 'group_count': group_count, 'repo_count': repo_count['repoCount__sum'], 'star_count': star_count['starCount__sum'], 'user_count': user_count})


def creategroup(request):
    form = GroupCreateForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        userId = form.cleaned_data['userId']
        groupName = form.cleaned_data['groupName']

        if User.objects.filter(groupName=groupName).exists():
            messages.success(request, f'{groupName} group Already Exists!')
            return redirect('creategroup')
        # hard coded input to test
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
            groupName=groupName,
            namegroupid=userId + "_" + groupName
        )
        messages.success(
            request, f'{groupName} created! {userId}, Invite your Friends')
        return redirect('groups')
    else:
        form = GroupCreateForm()
        group_count = len(User.objects.values_list('groupName').distinct())
        repo_count = User.objects.values('userId').distinct().annotate(
            total=Sum('repoCount')).aggregate(Sum('repoCount'))
        star_count = User.objects.values('userId').distinct().annotate(
            total=Sum('starCount')).aggregate(Sum('starCount'))
        user_count = len(User.objects.values_list('userId').distinct())
    return render(request, 'create.html', {'form': form, 'group_count': group_count, 'repo_count': repo_count['repoCount__sum'], 'star_count': star_count['starCount__sum'], 'user_count': user_count})


def about(request):
    return render(request, 'about.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, f'You account has been created successfully!')
            return redirect('login')
    else:
        form = UserRegisterForm()
        group_count = len(User.objects.values_list('groupName').distinct())
        repo_count = User.objects.values('userId').distinct().annotate(
            total=Sum('repoCount')).aggregate(Sum('repoCount'))
        star_count = User.objects.values('userId').distinct().annotate(
            total=Sum('starCount')).aggregate(Sum('starCount'))
        user_count = len(User.objects.values_list('userId').distinct())
    return render(request, 'register.html', {'form': form, 'group_count': group_count, 'repo_count': repo_count['repoCount__sum'], 'star_count': star_count['starCount__sum'], 'user_count': user_count})
