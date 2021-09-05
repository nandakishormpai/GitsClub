import requests
from datetime import date, timedelta


def getTotalUserStars(_users):
    user_starCount = {}
    for user in _users:
        response = requests.get(
            f"https://api.github.com/users/{user}/repos",
        )
        repos = response.json()
        star_count = 0
        for i in range(len(repos)):
            star_count = star_count + repos[i]["stargazers_count"]
        user_starCount.update({user: star_count})
    return user_starCount


def getRepoCount(_users):
    user_repoCount = {}
    for user in _users:
        response = requests.get(
            f"https://api.github.com/users/{user}/repos",
        )
        repos = response.json()
        user_repoCount.update({user: len(repos)})
    return user_repoCount


def getFollowerCount(_users):
    user_followerCount = {}
    for user in _users:
        response = requests.get(
            f"https://api.github.com/users/{user}/followers",
        )
        followerCount = len(response.json())
        user_followerCount.update({user: followerCount})
    return user_followerCount


def getUserEvents(_users):
    user_activity = {}
    for user in _users:
        response = requests.get(f"https://api.github.com/users/{user}/events/public")
        events = response.json()
        currentDate = date.today()
        for event in events:
            print(event["created_at"].split("T")[0])


def getUserInfo(_users):
    groupUserInfo = {}
    for user in _users:
        response = requests.get(
            f"https://api.github.com/users/{user}",
        )
        _userInfoResponse = response.json()

        groupUserInfo[user] = {}
        groupUserInfo[user]["name"] = _userInfoResponse["name"]
        groupUserInfo[user]["profileURL"] = _userInfoResponse["html_url"]
        groupUserInfo[user]["bio"] = _userInfoResponse["bio"]
        groupUserInfo[user]["profileImage"] = _userInfoResponse["avatar_url"]
        groupUserInfo[user]["repoCount"] = getTotalUserStars([user])[user]
        groupUserInfo[user]["starCount"] = getTotalUserStars([user])[user]
        groupUserInfo[user]["followerCount"] = getFollowerCount([user])[user]
    return groupUserInfo


if __name__ == "__main__":
    print(getUserEvents(["AntonySJohn"]))
