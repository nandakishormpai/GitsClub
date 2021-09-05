import requests
from datetime import datetime, timedelta,date


def getTotalUserStars(_users):
    user_starCount = {}
    for user in _users:
        response = requests.get(
            f"https://api.github.com/users/{user}/repos", headers={"Authorization":"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"}
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
            f"https://api.github.com/users/{user}/repos", headers={"Authorization":"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"}
        )
        repos = response.json()
        user_repoCount.update({user: len(repos)})
    return user_repoCount


def getFollowerCount(_users):
    user_followerCount = {}
    for user in _users:
        response = requests.get(
            f"https://api.github.com/users/{user}/followers", headers={"Authorization":"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"}
        )
        followerCount = len(response.json())
        user_followerCount.update({user: followerCount})
    return user_followerCount


def getUserEvents(_users):
    user_activity = {}
    for user in _users:
        response = requests.get(f"https://api.github.com/users/{user}/events/public", headers={"Authorization":"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"})
        events = response.json()
        currentDate = datetime.today()
        nextDate = currentDate + timedelta(days=1)
        currentDateCount = 0
        nextDateCount = 0
        for event in events:
            val = event["created_at"].split("T")[0]
            _date = datetime.strptime(val, "%Y-%m-%d")
            if(currentDate==_date):
                currentDateCount = currentDateCount + 1
            elif(nextDateCount==_date):
                nextDateCount = nextDateCount + 1
            else:
                break
        user_activity.update({user:(nextDateCount-currentDate/currentDate)*100})
    return user_activity



def getUserInfo(_users):
    groupUserInfo = {}
    for user in _users:
        response = requests.get(
            f"https://api.github.com/users/{user}", headers={"Authorization":"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"}
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
        groupUserInfo[user]["publicActivityDailyIncrement"] = getUserEvents([user])[user]
    return groupUserInfo


if __name__ == "__main__":
    print(getUserEvents(["AntonySJohn"]))
